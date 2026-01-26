# Basic Maths - Pattern Summary

## The One Core Pattern: Digit Extraction

Almost every problem here uses the same loop:

```python
while n > 0:
    digit = n % 10      # extract last digit
    n = n // 10         # remove last digit
    # do something with digit
```

This is the foundation. Master this, and you've mastered basic maths problems.

---

## Problems Covered

| Problem | Core Operation | Time | Space |
|---------|---------------|------|-------|
| Count Digits | Loop and count | O(d) | O(1) |
| Reverse Integer | Build number backwards | O(d) | O(1) |
| Palindrome | Reverse and compare | O(d) | O(1) |
| Armstrong | Sum of digits^k | O(d) | O(1) |
| Divisors/Prime | Loop to √n | O(√n) | O(1) |

Where d = number of digits

---

## Pattern 1: Digit Extraction (`% 10` and `// 10`)

**Used in:** Count digits, Reverse, Palindrome, Armstrong

```python
# Extract last digit
digit = n % 10    # 5873 % 10 = 3

# Remove last digit
n = n // 10       # 5873 // 10 = 587
```

**Mental model:** Think of `% 10` as "peel off" and `// 10` as "chop off"

---

## Pattern 2: Building a Number (`rev = rev * 10 + digit`)

**Used in:** Reverse Integer, Palindrome Check

```python
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit  # shift left, then add
    n = n // 10
```

**Why `* 10 + digit`?**
- `* 10` = shift existing digits left (make room)
- `+ digit` = place new digit in the ones place

Example: Building 321 from 123
```
rev = 0
rev = 0 * 10 + 3 = 3
rev = 3 * 10 + 2 = 32
rev = 32 * 10 + 1 = 321
```

---

## Pattern 3: Count Digits (Two Ways)

**Method 1: Loop**
```python
count = 0
while n > 0:
    n = n // 10
    count += 1
```

**Method 2: Math (O(1))**
```python
from math import log10
count = int(log10(n) + 1)
```

---

## Pattern 4: Loop to √n (Square Root Optimization)

**Used in:** Divisors, Prime Check

**Key insight:** Divisors come in pairs. If `i` divides `n`, then `n/i` also divides `n`.

```python
i = 1
while i * i <= n:    # only go up to √n
    if n % i == 0:
        # i is a divisor
        # n // i is also a divisor (the pair)
    i += 1
```

**Why stop at √n?**
- For n=36: pairs are (1,36), (2,18), (3,12), (4,9), (6,6)
- After 6, you'd find the same pairs in reverse
- 6 = √36, so stop there

**Prime check shortcut:**
```python
def isPrime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```

---

## Pattern 5: Overflow Protection (Interview Favorite)

**Used in:** Reverse Integer

Before doing `rev = rev * 10 + digit`, check:

```python
INT_MAX = 2**31 - 1
MAX_PREFIX = INT_MAX // 10  # 214748364
MAX_LAST = INT_MAX % 10     # 7

if rev > MAX_PREFIX:
    return 0  # will overflow
if rev == MAX_PREFIX and digit > MAX_LAST:
    return 0  # will overflow
```

**Memory hook:** "Check before you build, not after"

---

## Python Gotchas

1. **`^` is XOR, not power** — use `**` for exponent
2. **Negative modulo behaves differently** — use `abs(x)` first
3. **Integer division** — use `//` not `/`

---

## Quick Reference: When to Use What

| If you need to... | Use this pattern |
|-------------------|------------------|
| Extract each digit | `while n > 0: digit = n % 10; n //= 10` |
| Build a number from digits | `rev = rev * 10 + digit` |
| Count digits | `int(log10(n) + 1)` or loop |
| Find divisors | Loop to `i * i <= n`, check pairs |
| Check prime | Loop from 2 to √n, any divisor = not prime |
| Handle overflow | Check `rev > MAX // 10` before multiplying |

---

## One-Liner Summaries

- **Count Digits:** Keep dividing by 10 until gone
- **Reverse:** Peel from back, build from front
- **Palindrome:** Reverse it, compare to original
- **Armstrong:** Sum of (each digit ^ digit count) == original
- **Divisors:** Pairs up to √n, don't forget the partner
- **Prime:** No divisors from 2 to √n
