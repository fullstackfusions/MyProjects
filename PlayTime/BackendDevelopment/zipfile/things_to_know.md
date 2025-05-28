## 🚫 Why You Should Avoid `ZIP_DEFLATED` in Some Cases

`ZIP_DEFLATED` = Compression using zlib (default behavior), and has pros and cons.

### ✅ Use `ZIP_DEFLATED` When:
- You are archiving **text-based or highly compressible data**.
- You want smaller output files, and time isn't a critical factor.
- You are storing the file for **long-term storage** or **download** optimization.

### ❌ Avoid `ZIP_DEFLATED` When:
- You are working with **already compressed data** (e.g., `.jpg`, `.png`, `.mp4`, `.gz`, etc.) → negligible gain, extra CPU usage.
- You are **streaming large files** or doing real-time zipping → compression slows things down.
- You care more about **speed over storage size** → `ZIP_STORED` is faster and CPU-light.

---

### 🔄 Recommendation

| Scenario                         | Suggested Compression |
|----------------------------------|------------------------|
| CPU-bound tasks / Large data     | `ZIP_STORED`           |
| Highly compressible data (text)  | `ZIP_DEFLATED`         |
| Real-time streaming              | `ZIP_STORED`           |
| Upload-then-delete scenarios     | `ZIP_STORED`           |
