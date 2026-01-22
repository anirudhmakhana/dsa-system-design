# Time & Space Complexity Quiz

Test yourself! Try to answer before revealing the solution.

---

## Q1

```python
for i in range(n):
    for j in range(i):
        pass
```

**What is the time complexity and why?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n²)

The inner loop does not run `n` times every time.

Let's count actual work:

- when `i = 0` → inner loop runs 0 times
- when `i = 1` → runs 1 time
- when `i = 2` → runs 2 times
- ...
- when `i = n-1` → runs n-1 times

**Total operations:**

```
0 + 1 + 2 + ... + (n-1)
```

This sum is:

```
n(n-1)/2
```

Which simplifies to:

**O(n²)**

This is the classic triangular sum pattern. You'll see this in:
- Bubble sort
- Selection sort
- Checking all pairs

</details>

---

## Q2

```python
arr = []
for i in range(n):
    arr.append(i)
```

**Time complexity? Why is it not O(n²)?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n)

Each `append` is **amortized O(1)**.

**What actually happens:**

- `append` is amortized O(1)
- Resizing is rare and costs O(k)
- Total cost of all resizes across n appends is O(n)
- Therefore total time is O(n)

**The key sentence interviewers love:**

> "Although individual appends can be expensive due to resizing, the total cost over n appends is linear."

**Why it's NOT O(n²):**

The precise reason is:

> "Because the sum of all resize costs across the entire loop is O(n), not because each append is expensive."

This distinction shows deep understanding.

**Mental model to lock in:**

Imagine:
- Resizing doubles capacity
- Each element gets copied only a few times over its lifetime
- Not copied on every append

That's why amortized works.

**You'll see this pattern in:**
- Dynamic arrays
- Hash table resizing
- StringBuilder implementations

</details>

---

## Q3

```python
arr = [1, 2, 3, 4, 5]
for _ in range(n):
    if 3 in arr:
        pass
```

**What is the time complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n)

**Hidden trap:** `x in list` is linear, and it's inside a loop.

**What is actually happening:**

- `3 in arr` → arr is a list → Python checks one by one
- Cost = O(len(arr))
- len(arr) is constant here (5), so each check is O(1)
- You do it n times

**Total time:** n × O(1) = **O(n)**

---

### The Real Hidden Trap

This looks innocent, but if arr were large:

```python
arr = list(range(n))
for _ in range(n):
    if n-1 in arr:
        pass
```

Now:
- `in arr` is O(n)
- Loop runs n times
- Total: O(n × n) = **O(n²)**

**THAT is the trap.**

People read `if x in arr` and forget: "arr is a list, not a set"

---

### How to Fix It

Replace list with set:

```python
arr = set([1, 2, 3, 4, 5])
```

Now:
- Membership is O(1) average
- Loop n times → O(n)

---

### Mental Rule to Burn In

> If you see `x in something` inside a loop, ask: **is it a list or a set?**

That single question avoids a huge number of TLEs.

---

### Common Mistake

Thinking `if` statements cause exponential branching.

**Why this is NOT O(2^n):**

O(2^n) happens when each step branches into recursive calls and both branches continue expanding:

```python
def f(i):
    f(i+1)
    f(i+1)  # doubles work each level
```

An `if` statement by itself does not double work — it either executes or skips.

</details>

---

## Q4

```python
from collections import deque
q = deque()

for i in range(n):
    q.append(i)

for i in range(n):
    q.popleft()
```

**What is the time complexity? What is the space complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: Time O(n), Space O(n)

**Time complexity: O(n)**

- `append` is O(1)
- `popleft` is O(1)
- Each runs n times
- Total: O(n) + O(n) = **O(n)**

---

**Space complexity: O(n)**

This is the subtle part.

**Common mistake:** "No space will be occupied since all the appended will be popped"

**Why this is wrong:**

Imagine:
1. You start with an empty train
2. You add n train cars, one by one
3. Only after that do you start removing them
4. At the peak moment, the train has n cars

---

### Key Rule (Burn This In)

> **Space complexity cares about peak memory, not final memory.**

Even though the deque ends up empty, it temporarily holds n elements.

- Peak extra memory = n elements
- Space complexity = **O(n)**

---

### Interview-Grade Answer

> "Time complexity is O(n) since both append and popleft are O(1) and each is executed n times. Space complexity is O(n) because the deque holds up to n elements at its maximum size."

That answer is bulletproof.

</details>

---

## Q5

```python
s = ""
for i in range(n):
    s += str(i)
```

**What is the time complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n²)

`s += piece` in a loop is dangerous.

**The key fact:**

Strings in Python are **immutable**.

That means:
- You can't change an existing string
- Every `+=` creates a brand new string

---

### Explain Like You're 5

Imagine writing a sentence on paper.

Each time you want to add a word:
1. You rewrite the entire sentence from scratch
2. Then add the new word at the end

So if your sentence grows like this:

```
"0"
"01"
"012"
"0123"
...
```

You are rewriting:
- 1 character
- then 2
- then 3
- up to n

**Total characters rewritten:**

```
1 + 2 + 3 + ... + n = n(n+1)/2
```

That's **O(n²)**.

---

### What's Happening Technically

On each iteration:

```python
s = s + str(i)
```

Python must:
1. Allocate new memory for the combined string
2. Copy all characters from `s`
3. Copy characters from `str(i)`

Cost of iteration i ≈ O(i)

Sum of costs: O(1 + 2 + 3 + ... + n) = **O(n²)**

---

### Why This Tricks Engineers

This looks harmless because:
- There's only one loop
- No nested loops

But immutability turns it into hidden quadratic behavior.

**This is one of the most common Python TLE traps in interviews.**

---

### Mental Alarm to Install

> **String concatenation inside a loop = red flag**

Every time you see `s += something` inside a loop, your brain should scream:

🚨 **copying is happening**

---

### The Safe Version

```python
parts = []
for i in range(n):
    parts.append(str(i))
s = "".join(parts)
```

This:
- Appends to a list (amortized O(1))
- Joins once (O(total_chars))
- Overall: **O(n)** time

</details>

---

## Q6

```python
parts = []
for i in range(n):
    parts.append(str(i))
s = "".join(parts)
```

**What is the time and space complexity? Why is this better than Q5?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n) time, O(n) space

(Technically O(n + total_chars), but simplified for DSA discussions)

---

### Break It Into Two Phases

**1) Building parts**

```python
for i in range(n):
    parts.append(str(i))
```

- Loop runs n times
- `append` is amortized O(1)
- Converting `i` to string costs some characters, but overall proportional

👉 O(n) time, O(n) space for the list references

**2) `"".join(parts)`**

- Python allocates the final string once
- Copies each character exactly once

👉 O(total_chars) time, O(total_chars) space for the final string

**Combined:** O(n + total_chars) ≈ **O(n)**

---

### Why This is Better Than Q5

| Q5 (bad) | Q6 (good) |
|----------|-----------|
| `s += piece` | `parts.append(piece)` then `"".join(parts)` |
| Copies string every iteration | Cheap appends |
| 1 + 2 + 3 + ... + n work | One single copy at the end |
| **O(n²)** | **O(n)** |

**Core difference:**

- Q5 copies on every step
- Q6 copies exactly once

---

### Explain Like You're 5

**Q5** is like:
> Rewriting the whole book every time you add one sentence

**Q6** is like:
> Writing sentences on sticky notes, gluing them all together once at the end

---

### Mental Rule to Burn In

> **Build pieces in a list, glue once.**

Or even shorter:

> **Collect first, join once.**

This single rule saves you from a huge class of Python TLEs.

</details>

---

## Q7

```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return False
```

**What is the time and space complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: Time O(log n), Space O(1)

**Time: O(log n)** — Each iteration cuts the search space in half.

**Space: O(1)** — Only uses a constant number of variables.

---

### Why Space is O(1)

**Explain like you're 5:**

Imagine you are searching a book.

You keep:
- One left finger
- One right finger
- One middle finger

No matter how thick the book is, you never use more fingers.

That's constant space.

---

### What Space Complexity Actually Counts

Space complexity counts **extra memory that grows with input size**.

In this function, you only use:
- `l`, `r`, `m`

That's:
- A constant number of variables
- No new arrays
- No recursion stack

So space does not grow with n.

---

### Common Mistake: Confusing with Recursive Version

```python
def bs(arr, l, r):
    if l > r:
        return False
    m = (l + r) // 2
    if arr[m] == target:
        return True
    elif arr[m] < target:
        return bs(arr, m+1, r)
    else:
        return bs(arr, l, m-1)
```

This recursive version has:
- O(log n) time
- **O(log n) space** (call stack)

But the iterative version uses **O(1) space**.

---

### Mental Rule to Burn In

> **Loops reuse stack frames, recursion grows stack frames.**

Or even simpler:

> **Iteration = O(1) space unless you allocate.**

</details>

---

## Q8

```python
def foo(n):
    if n == 0:
        return
    foo(n - 1)
```

**What is the time and space complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: Time O(n), Space O(n)

**Time: O(n)** — Each call reduces n by 1, total calls = n, constant work per call.

**Space: O(n)** — Recursion depth is n, so call stack grows to n frames.

---

### Explain Like You're 5

Every time `foo` is called, you put a plate on a stack.

- First call → 1 plate
- Second call → 2 plates
- Third call → 3 plates
- ...
- nth call → n plates

You cannot remove a plate until the function returns.

So at the deepest point, you have **n plates stacked**.

---

### What Space Complexity Counts Here

Space complexity includes:
- Local variables
- **Call stack frames**

Each recursive call creates:
- A new stack frame
- Its own `n` value
- Return address

Number of frames = recursion depth = n

So: **Space = O(n)**

---

### Common Mistake: When is it O(log n)?

O(log n) space happens when recursion **halves** the problem each time:

```python
def foo(n):
    if n <= 1:
        return
    foo(n // 2)  # halving!
```

- Depth ≈ log n
- Space ≈ O(log n)

But in this question:
- n → n-1 → n-2 → ...
- Depth grows **linearly**

---

### Mental Rule to Burn In

> **Recursion space = maximum recursion depth**

Then ask:
- Does the input shrink by **half** → O(log n)
- Or by **1** → O(n)

---

### Interview-Ready Wording

> "Time complexity is O(n) since the function is called n times. Space complexity is O(n) due to the recursion call stack growing linearly."

</details>

---

## Q9

```python
seen = set()
for x in arr:
    if x in seen:
        return True
    seen.add(x)
```

**What is the time and space complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: Time O(n) average, Space O(n)

**Time: O(n) average case**
- Loop runs at most n times
- `x in seen` is O(1) average
- `seen.add(x)` is O(1) average
- Total: n × O(1) = O(n)

**Space: O(n)**
- In worst case, all numbers are unique
- You store all of them in the set

---

### Explain Like You're 5

Imagine a box where you put numbers you've already seen.

In the worst case:
- All numbers are unique
- You store all of them

So the box grows with input size.

👉 n items → O(n)

---

### The Assumption You Must Explicitly State

This is the part interviewers care about:

> We assume the hash function distributes keys well, so set operations are O(1) **on average**.

Without this assumption:
- Worst-case lookup can degrade to O(n)
- Total time could degrade to O(n²)

You don't need to go deep into adversarial hashing unless prompted, but mentioning "average case" is important.

---

### Interview-Ready Answer

> "Time complexity is O(n) on average since each membership check and insertion into the set is O(1) on average. Space complexity is O(n) because in the worst case we store all elements in the set. This assumes a well-distributed hash function."

That answer signals strong fundamentals.

</details>

---

## Q10

```python
arr.sort()
for i in range(n):
    pass
```

**What is the overall time complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n log n)

Sorting dominates the runtime.

---

### Break It Into Parts

**1) `arr.sort()`**
- Python uses Timsort
- Worst-case and average-case: O(n log n)
- Best-case (nearly sorted): O(n), but we don't assume that

**2) The loop**
```python
for i in range(n):
    pass
```
- Runs n times
- O(n)

---

### Combining Sequential Steps

When you combine steps sequentially, you take the **dominant term**:

```
O(n log n) + O(n) = O(n log n)
```

---

### Interview-Quality Phrasing

> "Sorting dominates the runtime. Since `arr.sort()` is O(n log n) and the following loop is O(n), the overall time complexity is O(n log n)."

---

### Bonus Point (Optional)

You could add:

> "In the best case, Timsort can be O(n) if the array is nearly sorted, but in general we consider O(n log n)."

This is not required, but it signals depth.

</details>

---

## Q11

```python
def f(n):
    for i in range(n):
        for j in range(100):
            pass
```

**What is the time complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n)

The inner loop has a **fixed bound**, so it's a constant.

---

### Break It Down

**Inner loop:**
```python
for j in range(100):
```
- Runs a fixed number of times
- Does not depend on n
- This is O(1), not O(n)

**Outer loop:**
```python
for i in range(n):
```
- Runs n times

**Total work:**
```
n × 100 = 100n
```

In Big-O, constants are dropped → **O(n)**

---

### Explain Like You're 5

Imagine:
- You walk down a line of n people
- For each person, you clap exactly 100 times

No matter how long the line gets:
- Clapping count never changes
- Only the number of people matters

So the work grows with n, not with 100.

---

### Key Rule to Burn In

> **Loops with fixed bounds are constants.**

Even if the number is large (10, 100, 1000) — as long as it does not depend on n, it's O(1).

---

### Interview Trap This Avoids

Many people mistakenly say:

> "Nested loop → O(n²)"

Not always! Only when **both loops** depend on input size.

</details>

---

## Q12

```python
heap = []
for x in arr:
    heapq.heappush(heap, x)
```

**What is the time complexity? Can it be improved?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n log n)

**Improvement:** Use `heapq.heapify(arr)` → O(n)

---

### What Actually Happens

`heapq.heappush(heap, x)` is O(log k) where k is the **current heap size**.

During the loop:
- First push → log(1)
- Second push → log(2)
- ...
- nth push → log(n)

**Total work:**
```
log(1) + log(2) + ... + log(n) = O(n log n)
```

---

### Why This is NOT O(n)

Even though the loop runs n times, the **cost per iteration grows** as the heap grows.

This is the key insight.

---

### Explain Like You're 5

Imagine stacking blocks into a pyramid:
- First block: easy
- Second block: adjust a little
- Bigger pyramid → more adjustments

Each new block may need to climb up the pyramid.

More blocks = more climbing = more steps.

---

### How to Improve (The Optimization)

```python
heapq.heapify(arr)
```

**Why this is faster:**

`heapify`:
- Starts from the bottom
- Fixes heap property downward
- Avoids repeated bubbling

**Total time: O(n)**

This is a very common interview optimization.

---

### Interview-Ready Answer

> "Pushing elements one by one into a heap takes O(n log n) time since each heappush is O(log n). This can be optimized to O(n) by using `heapq.heapify` to build the heap in linear time."

</details>

---

## Q13

```python
def subsets(nums):
    res = []
    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        backtrack(i + 1, path)           # skip
        path.append(nums[i])
        backtrack(i + 1, path)           # take
        path.pop()
    backtrack(0, [])
    return res
```

**What is the time and space complexity of generating all subsets?**

<details>
<summary>Click to reveal answer</summary>

### Answer: Time O(n · 2^n), Space O(n · 2^n)

---

### Why O(n · 2^n) Time

At each index you make two choices:
- Skip the element
- Take the element

This creates a **binary decision tree**.

**Breakdown:**
- Number of subsets of n items = 2^n
- You also do `path[:]` copy when you hit a leaf
- Copying costs O(k) where k is subset size
- Across all subsets, total copied elements = O(n · 2^n)

👉 **Time: O(n · 2^n)**

If you ignore output copying cost, you'll often hear O(2^n), but interview-clean is O(n · 2^n) because you're literally building and copying outputs.

---

### Space Complexity

Three "spaces" to think about:

| Component | Size |
|-----------|------|
| Recursion depth | O(n) stack |
| Path size | O(n) |
| Output `res` | 2^n subsets, O(n · 2^n) total elements |

👉 **Space including output: O(n · 2^n)**
👉 **Auxiliary space excluding output: O(n)**

---

### Why It Explodes

Every element doubles the number of possibilities.

n goes from 20 to 25 → work multiplies by 32.

**Mental picture:** Each element is a yes/no switch. n switches create 2^n combinations.

</details>

---

## Q14

```python
for i in range(n):
    for j in range(n):
        if i == j:
            break
```

**What is the time complexity?**

<details>
<summary>Click to reveal answer</summary>

### Answer: O(n²)

Even with the break, it's still quadratic.

---

### What Happens

For each `i`:
- `j` runs 0, 1, 2, ... until it hits `j == i`
- Then breaks

So inner loop runs `i + 1` times for a given `i`.

**Total work:**
```
(1 + 2 + 3 + ... + n) = n(n+1)/2
```

👉 **Time: O(n²)**

---

### Why It's Not "Full" n²

The break stops early, so it's not n steps for every i.

But it's still **quadratic** because the sum is triangular, not linear.

**Quick check:**
- If inner loop ran constant times → O(n)
- But it grows with i → O(n²)

---

### Triangular Sum Recognition

Whenever you see inner loop running up to `i`:

> "Sum 1..n = n(n+1)/2 = **O(n²)**"

This is the same pattern as Q1.

</details>

---

## Q15

**When do you say O(1) vs O(n) for hash table operations?**

<details>
<summary>Click to reveal answer</summary>

### Short Answer

- **Say O(1)** in typical interview/LeetCode context
- **Mention O(n) worst case** when asked or when guarantees matter

---

### Acceptable to Say "O(1)"

When:
- Discussing standard behavior of dict/set
- The problem is not adversarial
- Interview context is typical LeetCode style
- Constraints suggest they expect hashing

**Good phrasing:**
> "Average O(1) with a hash map/set"

---

### When to Mention Worst Case

Mention worst case when:
- Interviewer explicitly asks about worst case or guarantees
- Security or adversarial input context (hash flooding)
- Designing a system where worst-case latency matters
- Solution depends critically on O(1) and would fail badly otherwise

**Better phrasing:**
> "Average O(1), worst-case O(n) due to collisions, but in practice Python's hash table is designed to behave well."

**Showing depth:**
> "If worst-case matters, consider a balanced tree map, or constraints/assumptions that make hashing safe."

---

### Hash Phrasing Template (Memorize This)

> "Average O(1), worst O(n), acceptable unless adversarial or worst-case guarantees matter."

</details>

---

## Quick Drills to Lock In

### Drill 1: "Two recursive calls" = what?

If a function calls itself twice per level:
> "Binary tree growth, probably O(2^n)"

### Drill 2: Triangular sum recognition

If inner loop runs up to `i`:
> "Sum 1..n = n(n+1)/2 = O(n²)"

### Drill 3: Hash phrasing template

> "Average O(1), worst O(n), acceptable unless adversarial or worst-case guarantees matter."

---
