## What is memory-profiling:

Memory profiling is the process of measuring a program’s memory usage over time—both how much is allocated and where in your code those allocations happen. It helps you:

* **Detect Memory Leaks**
  Identify parts of your code that keep allocating without releasing memory.
* **Optimize Memory Footprint**
  Find hot spots where you’re over-allocating or holding onto large structures longer than needed.
* **Prevent OOM Crashes**
  In long-running services (web servers, workers), uncontrolled growth can eventually exhaust RAM.

---

memray and py-spy are both excellent profiling tools, but they serve different purposes:

## Memray:
- **Focus**: Deep memory profiling (allocation, leaks, memory usage over time)
- **Features**: Tracks memory allocations at python and native (C extension) levels, shows allocation call stacks, flamegraphs, and can identify leaks.
- **Overhead**: Higher than py-spy, but optimized for memory analysis.
- **Use case**: Find out where memory is being allocated, diagnose OOMs, memory leaks, or excessive memory usage.
- **How to use**: Run your script with `memray run your_script.py`, then analyze the output.

## py-spy:
- **Focus**: CPU profiling (function call time, performance bottlenecks).
- **Features**: Sampling profiler, very low overhead, can attach to running processes, supports flamegraphs.
- **Overhead**: Very low.
- **Use case**: Find out where your code spends time, diagnose slowdowns, performance bottlenecks.
- **How to use**: Run `py-spy top --pid <pid>` or `py-spy record -o profile.svg -- python your_script.py`

---

Below are two concrete examples—one using **py-spy** (primarily a sampling profiler, but which can also capture memory stats) and one using **Memray** (a dedicated memory profiler by Bloomberg).


## 1. Example with py-spy

> **Note:**
> py-spy’s main strength is CPU profiling, but recent versions can also sample the Python process’s resident set size (RSS) over time. You’ll get a timeline of memory usage alongside your CPU flame graph.

1. **Install**

   ```bash
   pip install py-spy
   ```

2. **Create a toy script** (`leaky.py`):

   ```python
   import time

   def leaky():
       data = []
       for i in range(10_000_00):
           data.append('x' * 100)   # allocate ~100 bytes each
       time.sleep(5)               # hold so profiler can sample

   if __name__ == "__main__":
       leaky()
   ```

3. **Run the script**:

   ```bash
   python leaky.py
   ```

   In another terminal, note the PID of that process:

   ```bash
   pgrep -f leaky.py
   ```

4. **Profile memory+CPU**:

   ```bash
   py-spy record \
     --pid <PID> \
     --native \
     --memory \
     --output profile.svg
   ```

   * `--memory` tells py-spy to sample the process’s RSS.
   * `--native` includes native stacks too.
   * You’ll get a `profile.svg` flame graph that shows CPU hot spots; hovering over the graph also shows memory usage at each sample point.

5. **Inspect**
   Open `profile.svg` in your browser. You’ll see:

   * The “width” of bands = proportion of CPU time.
   * Hover data includes the memory usage at that sample.

---

## 2. Example with Memray

Memray is a line-level, allocation-tracking profiler. It records every allocation and lets you see where memory was requested.

1. **Install**

   ```bash
   pip install memray
   ```

2. **Use the same `leaky.py`** (or any script you want to profile).

3. **Run under Memray**:

   ```bash
   memray run --native --format html -o memray_report.html python leaky.py
   ```

   * `--native` includes C-level allocations (e.g., library calls).
   * `--format html` produces a self-contained report.

4. **Open the report**

   ```bash
   xdg-open memray_report.html   # Linux
   open memray_report.html       # macOS
   ```

   The HTML report has sections:

   * **Allocation Timeline**: graph of total memory over time.
   * **Top Allocating Call Stacks**: shows which lines/functions allocated the most.
   * **Object Allocation Stats**: aggregate counts/sizes by module, function, or line.

5. **Command-line summary**
   If you prefer a terminal-only view:

   ```bash
   memray summary memray-report.bin
   ```

   This prints a table of “Top 10 allocation sites” with total bytes and counts.

---

### Putting It All Together

1. **Start with py-spy** when you want a quick, low-overhead look at both CPU and coarse memory trends.
2. **Use Memray** for in-depth, exact tracking of where allocations happen, at the cost of higher overhead.

By combining both, you can:

* **Pinpoint** “when” memory spikes occur (py-spy timeline).
* **Drill down** to “where” exactly in your code those allocations came from (Memray line-level).

Happy profiling!
