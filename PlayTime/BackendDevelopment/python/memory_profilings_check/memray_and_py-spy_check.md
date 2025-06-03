Below is a step-by-step “memory-profiling script” you can follow to learn both the coarse-grained, low-overhead approach with **py-spy** and the fine-grained, allocation-level approach with **Memray**. At each stage you’ll see what to run, what to look for, and which concepts to keep in mind.

---

## 1. Prerequisites

```bash
# Create & activate a virtualenv (optional, but recommended)
python3 -m venv venv && source venv/bin/activate

# Install profilers
pip install py-spy memray
```

> **Concepts to understand before you start**
>
> * **RSS vs. Allocations**
>
>   * RSS (Resident Set Size): total memory the process holds in RAM.
>   * “Allocations” tracked by Memray: every `malloc`/`PyObject_Malloc` call.
> * **Sampling vs. Tracing**
>
>   * Sampling (py-spy): periodically check call stacks + RSS → low overhead, coarse.
>   * Tracing (Memray): record every allocation site → high fidelity, higher overhead.
> * **Overhead**
>
>   * py-spy adds \~1–2% CPU overhead.
>   * Memray can slow your program by 10–30% depending on volume of allocations.

---

## 2. Prepare a Toy “Leaky” Script

Create `leaky.py`:

```python
import time

def allocate_leak(n):
    """Repeatedly build a list of strings and never free it."""
    data = []
    for i in range(n):
        data.append("x" * 1000)  # ~1 KB per entry
    # Hold for a while so profilers can sample
    time.sleep(3)

if __name__ == "__main__":
    allocate_leak(200_000)
```

> **What to notice**
>
> * The list `data` grows to \~200 MB.
> * There is no explicit `del`; until the function returns, memory stays allocated.

Run it normally:

```bash
python leaky.py
```

---

## 3. Coarse Profiling with **py-spy**

### 3.1. Start the target

```bash
python leaky.py &
LEAK_PID=$!
```

### 3.2. Record a combined CPU+Memory flame graph

```bash
py-spy record \
  --pid $LEAK_PID \
  --native \
  --memory \
  --rate 100 \
  --output pyspy-memory.svg
```

* `--memory` samples RSS every sample.
* `--rate 100` samples 100 times per second (default 100 Hz).
* `--native` includes C extension frames.

#### 3.3. Inspect `pyspy-memory.svg`

* **Width of each bar** → CPU time.
* **Hover tooltip** → shows RSS at that sample.
* **Key things to understand**

  * Spikes in RSS: when did most memory get allocated?
  * Which Python functions were “hot” at that time?
  * Sampling error: it may miss short-lived allocations.

---

## 4. Fine-Grained Profiling with **Memray**

### 4.1. Record all allocations

```bash
memray run \
  --native \
  --format html \
  -o memray-report.html \
  python leaky.py
```

* `--native` tracks C-level as well as Python allocations.
* `--format html` gives you a self-contained report.

### 4.2. Open the HTML report

```bash
open memray-report.html    # macOS
xdg-open memray-report.html # Linux
```

#### 4.3. Key sections to explore

1. **Allocation timeline**

   * Total memory over time → matches what you saw in py-spy.
   * Look for sudden jumps (large allocation bursts).

2. **Top allocating call stacks**

   * Which functions/lines called `malloc` most frequently or for largest bytes.
   * Drill down to see exact source lines.

3. **Object summaries**

   * Aggregate by module, function, or line.
   * Helps you spot “hot” sources of memory use.

4. **Flame graph** (Memray’s own)

   * Similar to CPU flame graph, but width = total bytes allocated in that frame.

### 4.4. Command-line summary (optional)

```bash
memray summary memray-report.bin
```

Outputs a table of the top 10 allocation sites by size/count.

---

## 5. What to Understand While Profiling

| Concept                      | Why It Matters                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| **Sampling Rate**            | Too low → miss short bursts; too high → overhead.                                  |
| **Overhead Budget**          | In production, you’ll prefer py-spy sampling; dev/staging → Memray.                |
| **Unreachable vs. Leaked**   | Python GC may free cycles; true leaks often live in C extensions or global caches. |
| **Breakdown by Call Site**   | Always drill from “when” (timeline) to “where” (call stack).                       |
| **Native vs. Python Frames** | Some heavy allocators live in C.                                                   |
| **Interpreting RSS Trends**  | RSS can include freed-but-not-returned-to-OS pages.                                |
| **Isolate Noise**            | Disable unrelated threads or modules to focus your area of interest.               |

---

## 6. Putting It All Together

1. **Start with py-spy**:

   * Low cost, quick view of overall memory timeline.
   * Identify rough hotspots.

2. **Switch to Memray**:

   * Deep dive into exact allocation sites.
   * Find leaking patterns (e.g. a cache that never evicts).

3. **Iterate**:

   * Fix the hot lines, re-benchmark.
   * Confirm that RSS no longer grows or major allocators have shrunk.

4. **Automate alerts** (optional):

   * Integrate a lightweight RSS sampler in your production service.
   * Trigger alert if RSS climbs >10% week-over-week.

---

By following this scripted workflow and keeping these concepts in mind, you’ll develop an intuition for “when” memory spikes occur and “where” they originate in your codebase. Happy profiling!
