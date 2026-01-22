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

---

# The Core Mental Model (This is Everything)

Before we even talk about list, dict, set, strings — lock in one rule:

> **Time complexity is about how much stuff has to physically move or be touched in memory.**
>
> Not abstract math. Actual movement. Actual touching.
>
> If something must slide, copy, or be searched, it costs time.

Keep that sentence in your head as we go.

---

## List (Dynamic Array) — Deep Dive

### How to Imagine a List

Imagine a row of boxes on the floor, perfectly lined up.

Each box:
- Has an index
- Is stored right next to the previous one

Python `list` is this row.

**Crucial Consequence:**

Because boxes are contiguous:
- Jumping to box 5 is instant
- Inserting a box in the middle forces everything to slide

This single fact explains almost every list complexity.

---

### `a[i]` get or set: O(1)

**Imagine:**

You want the toy in box 5.

You do not look at boxes 0 to 4.
You jump directly.

**Why:**

Indexing is just:
```
memory_start + (i × box_size)
```

No searching. No movement.

```python
arr = [10, 20, 30, 40, 50]

# O(1) - direct jump
value = arr[3]      # 40
arr[3] = 99         # instant update
```

> **Intuition Hook:** Jump, don't walk.

---

### `append(x)`: Amortized O(1)

**Imagine:**

You add a new box to the end of the row.

Usually:
- There is empty space at the end
- You just place it

Sometimes:
- The floor is full
- You rent a bigger floor
- Move all boxes
- Then continue

Most appends are cheap. Some are expensive. Overall average is cheap.

That is **amortized**.

```python
arr = [1, 2, 3]

arr.append(4)  # O(1) - just place at end
arr.append(5)  # O(1)
arr.append(6)  # O(1)
# occasionally triggers resize, but averaged out = O(1)
```

> **Intuition Hook:** Usually cheap, rarely painful.

---

### `pop()`: O(1)

**Imagine:**

You remove the last box.

Nothing else moves.

```python
arr = [1, 2, 3, 4, 5]

arr.pop()   # returns 5, arr is now [1, 2, 3, 4]
# nothing shifted
```

> **Intuition Hook:** End is safe.

---

### `insert(i, x)`: O(n)

**Imagine:**

You want to insert a new box at position 2.

You must:
1. Pick up box 2
2. Move it right
3. Move box 3 right
4. Move box 4 right
5. And so on...

Everything after index `i` shifts.

**Why this is O(n):**

In the worst case, you move almost all boxes.

```python
arr = [1, 2, 3, 4, 5]

arr.insert(2, 99)  # [1, 2, 99, 3, 4, 5]
# 3, 4, 5 all had to slide right
```

> **Intuition Hook:** Middle insert causes sliding.

---

### `pop(i)`: O(n)

Same idea as insert.

Removing from the middle leaves a hole.
Everything to the right must slide left.

```python
arr = [1, 2, 3, 4, 5]

arr.pop(1)  # removes 2, returns 2
# arr is now [1, 3, 4, 5]
# 3, 4, 5 all slid left
```

> **Intuition Hook:** Holes cause shifts.

---

### `x in a`: O(n)

**Imagine:**

You are checking if any box contains toy X.

You must:
1. Open box 0
2. Open box 1
3. Open box 2
4. Until you find it or reach the end

No shortcut.

```python
arr = [10, 20, 30, 40, 50]

if 30 in arr:       # O(n) - must check each element
    print("found")

if 99 in arr:       # O(n) - checks all, finds nothing
    print("found")
```

> **Intuition Hook:** Unsorted means search.

---

### `len(a)`: O(1)

**Imagine:**

There is a sticky note on the row that says:
"number of boxes = 7"

Python stores length separately.

```python
arr = [1, 2, 3, 4, 5]

n = len(arr)  # O(1) - reads stored value, doesn't count
```

> **Intuition Hook:** Length is remembered, not counted.

---

### Slicing `a[l:r]`: O(k) time and space

**Imagine:**

You want a smaller row from box `l` to box `r`.

Python must:
1. Create new boxes
2. Copy each item

`k` boxes copied means `k` work.

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sub = arr[2:6]  # [2, 3, 4, 5] - O(4) copies
```

**Critical Trap:**

Slicing inside loops silently adds extra O(n).

```python
# DANGER: O(n²) hidden
for i in range(len(arr)):
    sub = arr[i:]  # each slice is O(n-i)
```

> **Intuition Hook:** Slicing copies.

---

### Concatenation `a + b`: O(len(a) + len(b))

**Imagine:**

You want one longer row.

Python must:
1. Create a brand new row
2. Copy all of `a`
3. Copy all of `b`

Nothing is reused.

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b  # [1, 2, 3, 4, 5, 6]
# all 6 elements copied into new list
```

> **Intuition Hook:** New list, full copy.

---

### `reverse()`: O(n)

**Imagine:**

You swap:
- First with last
- Second with second-last
- And so on

You touch every element once.

```python
arr = [1, 2, 3, 4, 5]

arr.reverse()  # [5, 4, 3, 2, 1]
# in-place, but touches all elements
```

> **Intuition Hook:** Touch all to flip.

---

### `sort()`: O(n log n)

**Imagine:**

Python sorts by:
1. Finding already sorted chunks
2. Merging them efficiently

It still needs:
- log n levels of organization
- Touching all elements per level

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6]

arr.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]
# O(n log n) but highly optimized Timsort
```

**Important Interview Fact:**

Python sort is extremely optimized. Use it unless forbidden.

> **Intuition Hook:** Organize, then walk.

---

### Big Reminder (Burn Into Brain)

> **List is good at the end, bad at the front.**

That single sentence explains:
- `append` vs `pop(0)`
- Stack vs queue
- Why `deque` exists

```python
# GOOD - O(1)
arr.append(x)
arr.pop()

# BAD - O(n)
arr.insert(0, x)  # everything shifts
arr.pop(0)        # everything shifts
```

---

## Deque (Double-Ended Queue) — Deep Dive

### How to Imagine Deque

Imagine a **train**, not boxes on the floor.

Each car knows:
- Who is before
- Who is after

You can:
- Attach a car to front
- Attach a car to back
- Remove from front or back

**No sliding ever.**

```python
from collections import deque

dq = deque([1, 2, 3])
```

---

### `append` / `appendleft`: O(1)
### `pop` / `popleft`: O(1)

Nothing shifts. Links are updated.

```python
from collections import deque

dq = deque([1, 2, 3])

dq.append(4)       # [1, 2, 3, 4] - O(1)
dq.appendleft(0)   # [0, 1, 2, 3, 4] - O(1)

dq.pop()           # returns 4 - O(1)
dq.popleft()       # returns 0 - O(1)
```

> **Intuition Hook:** No sliding, just relinking.

---

### Indexing `d[i]`: O(n)

Deque is not meant for jumping.

You must walk car by car.

```python
dq = deque([1, 2, 3, 4, 5])

val = dq[3]  # O(n) - walks through links
# works, but don't use deque for random access
```

> **Intuition Hook:** Deque walks, list jumps.

---

### When to Use Deque

- BFS
- Sliding window
- Real queues

**Never use list for queue behavior.**

```python
from collections import deque

# BFS pattern - CORRECT
queue = deque([start])
while queue:
    node = queue.popleft()  # O(1)
    for neighbor in get_neighbors(node):
        queue.append(neighbor)

# WRONG way with list
queue = [start]
while queue:
    node = queue.pop(0)  # O(n) - SLOW!
```

---

## Dict (Hash Map) — Deep Dive

### How to Imagine Dict

Imagine a mail room with numbered lockers.

You:
1. Hash the key
2. Go to locker number
3. Open it

You do not search all lockers.

```python
d = {"alice": 100, "bob": 200, "charlie": 300}
```

---

### `d[key]` get/set: O(1) average

Hash → jump → done.

```python
d = {}

d["name"] = "alice"  # O(1) - hash "name", jump to locker
value = d["name"]    # O(1) - same jump
```

**Why "average":**

Sometimes lockers get crowded and resizing happens.
But over time, it balances out.

> **Intuition Hook:** Key decides the jump.

---

### `key in d`: O(1)

Same jump, just checking existence.

```python
d = {"a": 1, "b": 2, "c": 3}

if "b" in d:    # O(1) - hash and check
    print("found")

if "z" in d:    # O(1) - hash, check, not found
    print("found")
```

---

### Resizing (Amortized)

When lockers fill up:
1. Build a bigger mail room
2. Reassign lockers

Rare, but expensive. Overall still cheap.

---

### Use Dict For

- Counting
- Memoization
- Mapping identifiers

```python
# Counting frequency - O(n)
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

# Memoization
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

> **Intuition Hook:** Name to thing, instantly.

---

## Set (Hash Set) — Deep Dive

### How to Imagine Set

Same lockers as dict, but only names. No values.

```python
s = {1, 2, 3, 4, 5}
```

---

### `x in s`, `add`, `remove`: O(1) average

Same hash jump.

```python
s = {1, 2, 3}

s.add(4)         # O(1)
s.remove(2)      # O(1)
exists = 3 in s  # O(1) - True
```

---

### Set Operations Intuition

| Operation | What Happens | Complexity |
|-----------|--------------|------------|
| `a \| b` union | Touch everything in both | O(len(a) + len(b)) |
| `a & b` intersection | Touch smaller one | O(min(len(a), len(b))) |
| `a - b` difference | Scan one, check in other | O(len(a)) |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b  # {1, 2, 3, 4, 5, 6} - union
a & b  # {3, 4} - intersection
a - b  # {1, 2} - difference
```

> **Intuition Hook:** Hash lookup is cheap, scanning is not.

---

### Use Set For

- Visited tracking
- Deduping
- Fast membership checks

```python
# Visited in BFS/DFS
visited = set()
visited.add(node)
if neighbor not in visited:
    # process

# Deduping
unique = list(set(arr))

# Fast membership in loop - O(n) total instead of O(n²)
lookup = set(arr)
for x in other_arr:
    if x in lookup:  # O(1)
        print("found")
```

---

## Strings (The Silent Killer) — Deep Dive

### Strings are Immutable

This is non-negotiable.

**Once created, a string never changes.**

```python
s = "hello"
# s[0] = "H"  # ERROR - cannot modify
s = "H" + s[1:]  # creates NEW string
```

---

### `s[i]`, `len(s)`: O(1)

Same as list indexing.

```python
s = "hello"

char = s[2]      # 'l' - O(1)
length = len(s)  # 5 - O(1)
```

---

### `s + t`: O(len(s) + len(t))

New string is created. Old ones untouched.

```python
a = "hello"
b = "world"

c = a + b  # "helloworld" - new string created
# a and b still exist unchanged
```

---

### Repeated `s += piece`: O(n²) Trap

**Imagine:**

Every time you add a piece, copy everything again.

Looping this causes: 1 + 2 + 3 + ... + n copies

That is **quadratic**.

```python
# WRONG - O(n²)
s = ""
for word in words:
    s += word  # copies entire string each time!

# With 1000 words, you copy:
# 1 + 2 + 3 + ... + 1000 = ~500,000 operations
```

---

### `''.join(list)`: O(total_chars)

Join allocates once, copies once.

```python
# CORRECT - O(n)
words = ["hello", "world", "foo", "bar"]
result = ''.join(words)  # "helloworldfoobar"

# Building with separator
result = ' '.join(words)  # "hello world foo bar"
```

> **Intuition Hook:** Collect, then glue once.

---

### Slicing `s[l:r]`: O(k)

Copies characters.

```python
s = "hello world"
sub = s[0:5]  # "hello" - O(5) new string created
```

---

### `substring in s`

Can be expensive. Optimized internally, but don't rely on it.

```python
s = "hello world"

if "wor" in s:  # roughly O(n*m) worst case
    print("found")
```

---

### Interview Safe Rule

> **Build strings using list, then join.**

```python
# Pattern for building strings
parts = []
for item in items:
    parts.append(process(item))
result = ''.join(parts)
```

---

## Heapq (Binary Heap) — Deep Dive

### How to Imagine Heap

Imagine a **pyramid**.

Smallest element always at the top.

```python
import heapq

heap = []
```

---

### `heappush` / `heappop`: O(log n)

You:
1. Place item at bottom
2. Bubble up or down

Height of pyramid is log n.

```python
import heapq

heap = []

heapq.heappush(heap, 5)   # O(log n)
heapq.heappush(heap, 2)   # O(log n)
heapq.heappush(heap, 8)   # O(log n)
heapq.heappush(heap, 1)   # O(log n)

# heap internally: [1, 2, 8, 5]

smallest = heapq.heappop(heap)  # 1, O(log n)
```

---

### `heapify`: O(n)

Bulk construction is optimized.

```python
import heapq

arr = [5, 2, 8, 1, 9, 3]
heapq.heapify(arr)  # O(n) - converts in-place

# arr is now a valid heap: [1, 2, 3, 5, 9, 8]
```

---

### Use Heap For

- Top k problems
- Scheduling
- Merging sorted streams

```python
import heapq

# Top K smallest
def k_smallest(arr, k):
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(k)]  # O(k log n)

# Top K largest (use negative values)
def k_largest(arr, k):
    return heapq.nlargest(k, arr)  # O(n + k log n)
```

---

## Sorting — Deep Dive

### `sorted` vs `list.sort`

Both:
- O(n log n)
- Extremely optimized

```python
arr = [3, 1, 4, 1, 5, 9]

# sorted() - returns new list
new_arr = sorted(arr)  # arr unchanged

# list.sort() - in-place
arr.sort()  # arr is now sorted
```

Python uses **Timsort**:
- Exploits partial order
- Nearly O(n) if almost sorted

---

## Generators and Itertools — Deep Dive

### How to Imagine Generators

A **conveyor belt**, not a pile.

Items come one at a time.

```python
# Generator - produces items on demand
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Only one item in memory at a time
for x in count_up(1000000):
    process(x)
```

**Tradeoff:**
- Saves memory
- Can be slower per item

Use when memory matters.

---

## Copying — Deep Dive

### `a.copy()` or `a[:]`: O(n)

New objects created.

```python
original = [1, 2, 3, 4, 5]

copy1 = original.copy()  # O(n)
copy2 = original[:]      # O(n)
copy3 = list(original)   # O(n)
```

### `deepcopy`

Walks entire structure. Can explode.

```python
import copy

nested = [[1, 2], [3, 4], [5, 6]]

shallow = nested.copy()        # inner lists shared!
deep = copy.deepcopy(nested)   # everything copied
```

---

## Final Mental Model (Burn This In)

| Structure | Key Insight |
|-----------|-------------|
| **list** | jump fast, slide slow |
| **deque** | slide never, jump slow |
| **dict/set** | hash jump |
| **string** | immutable, copying hurts |
| **heap** | bubble up/down |
| **slicing** | copying |
| **append** | amortized |
| **pop(0)** | death |

```python
# The death trap everyone falls into
arr = [1, 2, 3, 4, 5]

# This is O(n²) for processing n items:
while arr:
    item = arr.pop(0)  # O(n) each time!

# This is O(n):
from collections import deque
dq = deque([1, 2, 3, 4, 5])
while dq:
    item = dq.popleft()  # O(1) each time
```
