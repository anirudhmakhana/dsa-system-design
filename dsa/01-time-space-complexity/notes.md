# Time and Space Complexity (The Real Understanding)

## What Complexity is Actually Measuring

Complexity is about **how work grows with input size n**, not how long it takes on your laptop.

- **Time Complexity**: roughly how many "basic operations" happen
- **Space Complexity**: how much extra memory you allocate (not counting the input itself)

You use complexity to answer:
- Will this die at n = 10^5?
- Is this safe in Python?
- What's the tradeoff between time and memory?

---

## Big-O, Big-Theta, Big-Omega

You'll mostly use Big-O, but it helps to know the trio:

| Notation | Meaning |
|----------|---------|
| O(f(n)) | Upper bound (grows no faster than) |
| Θ(f(n)) | Tight bound (grows like) |
| Ω(f(n)) | Lower bound (grows at least like) |

In interviews, you usually say:
- Worst-case time: O(...)
- Worst-case space: O(...)

---

## The "Dominant Term" Rule (Why We Ignore Constants)

If your runtime is:
- `3n + 50` → O(n)
- `2n² + 10n + 7` → O(n²)

Because for big n, the largest growth term dominates.

> **But as a backend engineer, you already know the hidden truth:**
> Constants matter. In interviews, Big-O is the language. In systems, you care about constant factors too.

---

## O(1) — Constant Time

### "Grab from your pocket"

**Imagine this:**

You have a backpack with one front pocket.
Someone asks: "What's inside the pocket?"

You don't search.
You just reach in.

Doesn't matter if the world has 10 toys or 10 million toys.

**Technical Examples:**
- Accessing `arr[5]`
- Reading `dict[key]`
- Checking `len(arr)`

**Python Mental Model:**
```python
x = arr[5]
```
This does not depend on array size.

**DSA Connection:**
- Array indexing
- Hash map lookups
- Heap peek

**Gut Feeling:** Size doesn't matter.

---

## O(log n) — Logarithmic Time

### "Cut it in half until it disappears"

**Imagine this:**

You're finding a word in a dictionary.

You open the middle:
- Too early → throw away half
- Too late → throw away half

Each step kills half the problem.

**Technical Examples:**
- Binary search on sorted array
- Search in a balanced BST
- Heap push/pop

**Python Mental Model:**
```python
while range not empty:
    cut search space in half
```

**Why it's insanely fast:**
- n = 1,000,000 → log₂(n) ≈ 20
- Doubling n adds one step

**DSA Connection:**
- Binary search
- Balanced trees

**Gut Feeling:** Problem shrinks faster than you can notice.

---

## O(n) — Linear Time

### "Walk the line once"

**Imagine this:**

You're checking if anyone in a line is wearing red shoes.

You look at each person once.
No jumping. No skipping.

**Technical Examples:**
- Finding max/min in array
- Counting frequency
- Checking if an element exists

**Python Mental Model:**
```python
for x in arr:
    do_something(x)
```

**DSA Connection:**
- Array traversal
- Prefix sums
- Two pointers (often)

**Gut Feeling:** One look per item. Fair and safe.

---

## O(n log n) — Linearithmic Time

### "Organize then sweep"

**Imagine this:**

You're sorting students by height.

1. Split them into smaller groups
2. Sort each group
3. Merge everything neatly

You touch everyone, but you do it smartly.

**Technical Examples:**
- Merge sort
- Heap sort
- Quicksort (average)

**Python Mental Model:**
```python
arr.sort()
```

**Why this is the "gold standard":**
- Best possible for comparison-based sorting
- Scalable to large inputs
- Acceptable in almost all interviews

**DSA Connection:**
- Sorting solutions
- Interval problems
- Greedy algorithms

**Gut Feeling:** Touch everything, but intelligently.

---

## O(n²) — Quadratic Time

### "Everyone talks to everyone"

**Imagine this:**

You're in a room of people.

Each person shakes hands with every other person.

That's a lot of handshakes.

**Technical Examples:**
- Checking all pairs
- Brute-force two-sum
- Nested loops over same array

**Python Mental Model:**
```python
for i in range(n):
    for j in range(n):
        do_something()
```

**When this hurts:**
- n = 10^4 → 100 million operations
- Python starts choking

**DSA Connection:**
- Brute-force solutions
- Naive DP
- Comparing all combinations

**Gut Feeling:** Fine for small rooms, chaos for crowds.

---

## O(2^n) — Exponential Time

### "Every yes/no choice doubles the world"

**Imagine this:**

You have n switches.

Each switch: on or off

Number of possible configurations:
`2 × 2 × 2 × ... × 2 = 2^n`

**Technical Examples:**
- Generating all subsets
- Naive recursion without memoization
- Knapsack brute force

**Python Mental Model:**
```python
for each element:
    choose to include or exclude
    # choices explode
```

**Scale:**
- n = 20 → ~1 million cases
- n = 30 → ~1 billion cases

**DSA Connection:**
- Backtracking
- Subset generation
- Brute-force recursion

**Gut Feeling:** Choices multiply faster than you can think.

---

## O(n!) — Factorial Time

### "Every possible ordering"

**Imagine this:**

You have n people.
You want every possible seating order.

- n = 3 → 6 ways
- n = 5 → 120 ways
- n = 10 → 3.6 million ways

**Technical Examples:**
- Generating all permutations
- Traveling salesman brute force

**Python Mental Model:**
```python
pick one element
permute the rest
repeat for all choices
```

**Why this is nuclear:**
Factorial grows faster than exponential.

**DSA Connection:**
- Permutation problems
- Brute-force scheduling

**Gut Feeling:** Combinatorial explosion.

---

## Growth Comparison (Visualize Forever)

Imagine **n = 1,000**:

| Complexity | Steps |
|------------|-------|
| O(1) | instant |
| O(log n) | ~10 steps |
| O(n) | 1,000 steps |
| O(n log n) | ~10,000 steps |
| O(n²) | 1,000,000 steps |
| O(2^n) | impossible |
| O(n!) | absurd |

---

## One-Sentence Memory Hooks

| Complexity | Hook |
|------------|------|
| O(1) | grab |
| O(log n) | halve |
| O(n) | walk |
| O(n log n) | sort |
| O(n²) | compare all |
| O(2^n) | choose or skip |
| O(n!) | arrange everything |

---

## Time Complexity of Common Python Operations

These are "expected" complexities in CPython. Real-world can vary, but this is the mental model you use.

---

### List (Dynamic Array)

| Operation | Complexity | Notes |
|-----------|------------|-------|
| `a[i]` get/set | O(1) | |
| `append(x)` | O(1) amortized | |
| `pop()` | O(1) | |
| `insert(i, x)` | O(n) | shifts elements |
| `pop(i)` | O(n) | shifts elements |
| `x in a` | O(n) | linear search |
| `len(a)` | O(1) | |
| `a[l:r]` slicing | O(k) | time and space, where k = r-l |
| `a + b` concatenation | O(len(a)+len(b)) | |
| `reverse()` | O(n) | |
| `sort()` | O(n log n) | average/worst, highly optimized Timsort |

> **Big Interview Reminder:**
> If you need queue behavior, **do not use list with `pop(0)`**.

---

### Deque (Double-Ended Queue) — `from collections import deque`

| Operation | Complexity |
|-----------|------------|
| `append`, `appendleft` | O(1) |
| `pop`, `popleft` | O(1) |
| `d[i]` indexing | O(n) — not meant for random access |

**Use deque for:**
- BFS
- Sliding window pops from left
- Any real queue

---

### Dict (Hash Map)

**Average case:**

| Operation | Complexity |
|-----------|------------|
| `d[key]` get/set | O(1) |
| `key in d` | O(1) |
| `del d[key]` | O(1) |

**Notes:**
- Worst-case can degrade, but usually ignored in interviews
- Resizing happens occasionally (amortized behavior)

**Use dict for:**
- Frequency counts
- Memoization
- Mapping ids to objects

---

### Set (Hash Set)

**Average case:**

| Operation | Complexity |
|-----------|------------|
| `x in s` | O(1) |
| `add`, `remove`, `discard` | O(1) |

**Set operations:**

| Operation | Complexity |
|-----------|------------|
| `a \| b` union | O(len(a)+len(b)) |
| `a & b` intersection | O(min(len(a), len(b))) typical |
| `a - b` difference | O(len(a)) typical |

**Use set for:**
- Visited nodes
- Deduping
- Membership checks in loops

---

### Strings (Important Because They Bite People)

**Strings are immutable in Python.**

| Operation | Complexity | Notes |
|-----------|------------|-------|
| `s[i]` | O(1) | |
| `len(s)` | O(1) | |
| `s + t` concatenation | O(len(s)+len(t)) | creates new string |
| `s += piece` in a loop | O(n²) overall | danger zone |
| `''.join(list_of_strings)` | O(total_chars) | best practice |
| `s[l:r]` slicing | O(k) | creates a new string |
| `substring in s` | ~O(n*m) worst | optimized in practice |

> **Interview Safe Rule:**
> Build strings using **list + join**.

---

### Heapq (Binary Heap)

| Operation | Complexity |
|-----------|------------|
| `heappush` | O(log n) |
| `heappop` | O(log n) |
| `heapify(list)` | O(n) |
| `heap[0]` peek min | O(1) |

**Use heap for:**
- Top k problems
- K-way merge
- Scheduling by smallest next time

---

### Sorting

| Operation | Time | Space |
|-----------|------|-------|
| `sorted(iterable)` | O(n log n) | O(n) extra |
| `list.sort()` | O(n log n) | in-place (mostly) |

**Timsort special advantage:**
If data is partially sorted, it can be closer to O(n).

---

### Itertools and Generators (Quick Reality)

- Generators can save memory (space)
- But might not be faster than lists in tight loops
- Use them when you truly benefit from streaming or memory constraints

---

### Copying

| Operation | Complexity |
|-----------|------------|
| `a.copy()` or `a[:]` | O(n) time and space |
| `copy.deepcopy` | Much more expensive, depends on structure |
