---
type: atomic
---
**Permanent Note: Python Data Structures – Lists, Tuples, Dicts & Sets**  
**Focus**: Time & space complexity analysis, slicing, shallow vs. deep copy  
**Created**: 30 March 2026  
**Tags**: #python #data-structures #performance #copy-semantics #sequences #hashables  
**Source/Context**: Core Python 3.12+ (CPython implementation). This note synthesizes official docs, *Fluent Python* (Ramalho), *Python Cookbook*, and practical benchmarking patterns. Useful for algorithm interviews, performance-critical code, and understanding why certain structures "feel" slow in real projects (e.g., large datasets, nested objects, or loops).

### 1. Quick Overview & When to Choose Each (High-Level Decision Framework)
- **List** (`[]`): Mutable, ordered sequence. Dynamic array under the hood. Best for: ordered data you need to modify frequently (append/pop/insert).
- **Tuple** (`()`): Immutable, ordered sequence. Fixed-size array. Best for: constants, function returns, hashable keys, or "write-once" data (thread-safe, memory-efficient).
- **Dict** (`{}`): Mutable, ordered (insertion order guaranteed since Python 3.7) hash map. Best for: fast lookups by key, counting, caching.
- **Set** (`set()` or `{}`): Mutable, unordered hash set (unique elements). Best for: membership testing, deduplication, set operations (union/intersection).

**Nuance/Implication**: Choice affects not just speed but also memory and thread-safety. In data-heavy apps (e.g., processing millions of records in Dhaka-based analytics pipelines), the wrong structure can turn O(n) into O(n²) accidentally.

### 2. Time & Space Complexity Analysis
All complexities are average-case (worst-case noted). Space is additional to the elements themselves.

| Operation                  | List                  | Tuple                | Dict                  | Set                   |
|----------------------------|-----------------------|----------------------|-----------------------|-----------------------|
| **Access by index**       | O(1)                 | O(1)                | N/A                  | N/A                  |
| **Access by key**         | N/A                  | N/A                 | O(1) avg, O(n) worst | O(1) avg, O(n) worst |
| **Membership (`in`)**     | O(n)                 | O(n)                | O(1) avg             | O(1) avg             |
| **Append / Add**          | O(1) amortized      | N/A (immutable)     | O(1) amortized       | O(1) amortized       |
| **Insert at position**    | O(n)                 | N/A                 | N/A                  | N/A                  |
| **Delete by index/key**   | O(n)                 | N/A                 | O(1) avg             | O(1) avg             |
| **Pop last**              | O(1)                 | N/A                 | N/A                  | N/A                  |
| **Iteration**             | O(n)                 | O(n)                | O(n)                 | O(n)                 |
| **Sort**                  | O(n log n)           | N/A (create new)    | N/A (use sorted())   | N/A                  |
| **Copy (shallow)**        | O(n)                 | O(n)                | O(n)                 | O(n)                 |

**Space Complexity** (for n elements):
- List/Tuple: O(n) + overallocation (lists overallocate ~1.125× for growth).
- Dict/Set: O(n) but higher constant factor (hash table load factor ~2/3, plus hash overhead). Sets are slightly lighter than dicts.
- **Edge case**: Very large n (10^6+): dicts/sets use ~3–5× more RAM than lists due to hashing. Tuples save ~10–20% vs. lists (no mutation overhead).

**Nuances & Gotchas**:
- **Amortized O(1) for append**: Lists resize by doubling (or similar). Worst-case resize is O(n) but rare → average O(1).
- **Worst-case O(n) for dict/set**: Hash collisions (rare in modern Python with siphash). Still, never rely on it for security-critical code.
- **Hashable requirement**: Only immutable + hashable objects can be dict keys or set elements (tuples ok if they contain only hashables; lists never).
- **Implication**: In performance-critical loops (e.g., game AI or data processing), prefer dict/set for lookups over list `in` checks. A common refactor: list → set can speed up membership 100–1000×.

### 3. Slicing (`[start:stop:step]`)
Slicing creates a **new** object (shallow copy of references). Works on **sequences only** (lists, tuples, strings, ranges). Dicts/sets do **not** support slicing.

- **Syntax**: `seq[start:stop:step]` (defaults: start=0, stop=len, step=1).
- **Time complexity**: O(k) where **k** = number of elements in the slice (not O(n)). Copies only the selected portion.
- **Space**: O(k).

**Examples**:
```python
lst = [0, 1, 2, 3, 4, 5]
print(lst[1:4])      # [1, 2, 3] → O(3)
print(lst[::2])      # [0, 2, 4] → every other
print(lst[::-1])     # [5, 4, 3, 2, 1, 0] → reverse (common idiom, still O(n))
tup = (10, 20, 30)
print(tup[:2])       # (10, 20) – new tuple
```

**Nuances & Edge Cases**:
- Negative indices: `lst[-3:]` = last 3 elements (works on tuples too).
- Empty slice: `lst[5:5]` = `[]` (no error).
- Step < 0: reverses direction.
- **Dict/Set limitation**: Use `list(d.keys())[:5]` or `dict(itertools.islice(d.items(), 5))` as workaround (extra O(n) cost).
- **Memory implication**: Slicing large lists creates full copies → for huge data, use `itertools.islice` (lazy, O(1) space) or views (e.g., `dict.keys()` is a dynamic view, no copy).
- **Performance tip**: In hot loops, avoid repeated slicing; prefer indices or generators.

### 4. Shallow vs. Deep Copy
Critical for mutable nested structures. Affects lists, dicts, sets (tuples are immutable so "copy" is usually just reference).

- **Shallow copy** (`copy.copy()`, `list()`, `dict()`, `set()`, or slicing `[:]`):
  - Copies the **top-level** container.
  - Nested mutable objects are **references** (shared).
  - Fast: O(n) time/space.

- **Deep copy** (`copy.deepcopy()`):
  - Recursively copies **everything**, including nested objects.
  - Fully independent structure.
  - Slower: O(n + size of all nested objects). Can be expensive or infinite-loop on recursive structures.

**Code Examples** (with behavior):
```python
import copy

# Shallow
original = [[1, 2], [3, 4]]
shallow = original[:]          # or copy.copy(original) or list(original)
shallow[0][0] = 99
print(original)   # [[99, 2], [3, 4]]  ← mutated! (shared inner list)

# Deep
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)   # [[99, 2], [3, 4]]  ← unchanged
```

**Edge Cases & Gotchas**:
- Tuples: `tuple(lst)` is shallow (inner mutables still shared). Use `copy.deepcopy` if needed.
- Dicts/Sets with nested lists: same issue.
- Custom objects: `__copy__` / `__deepcopy__` methods can be overridden (rare but important in libraries).
- Circular references: `deepcopy` handles them safely (uses memo dict).
- **Performance implication**: In recursive data (trees, graphs) or large JSON-like structures, shallow copy is usually what you want for speed; deep copy only when you *must* mutate independently.
- **Memory implication**: Deep copy can explode RAM on deeply nested or large data (e.g., 10k nested dicts).

**When it bites you**: API responses (JSON → dict of lists), game state (player inventories), or ML data pipelines. Always ask: "Will I mutate the copy?"

### 5. Broader Implications, Edge Cases & Best Practices
- **Thread-safety**: Tuples & frozen sets are safer in multi-threaded code (no mutation). Lists/dicts need locks.
- **Memory profiling**: Use `sys.getsizeof()` + `pympler` for real usage. Dicts/sets have high overhead.
- **Python version note**: Pre-3.7 dicts were unordered; post-3.7+ they preserve order (but still not a list).
- **Common pitfalls**:
  - Using mutable as default function arg (classic bug: `def f(x=[])`).
  - Modifying list while iterating (use copy or list comprehension).
  - Assuming set order (never).
- **Real-world scaling**: For 10^5+ elements, profile with `timeit` or `cProfile`. Lists win for sequential access; hash structures win for random access.
- **Related concepts**: View objects (`dict.keys()`), `collections` (deque, defaultdict, Counter), `array` module for memory-tight numeric lists.
- **Question for future notes**: How do these compare to NumPy arrays or Pandas structures for data science? (Hint: NumPy slicing is also O(k) but views are possible.)
