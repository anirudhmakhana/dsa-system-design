"""

Given an integer n, return all the divisors of n.

Example 1:
Input: n = 12
Output: 6

When you see a divisor problem, think:

divisors come in pairs

finding one gives the other for free

stop when the left side would cross the right

watch out for perfect squares

If you can say those four things, you understand divisor problems.
"""
class Solution:
    def listDivisors(self, n: int) -> list[int]:
        if n <= 0:
            return []  # or raise ValueError depending on your needs

        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        return sorted(divisors)

    def countDivisors(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                count += 1            # i
                if i != n // i:
                    count += 1        # n//i
            i += 1
        return count

    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(f"12 -> {sol.listDivisors(12)}")  # [1, 2, 3, 4, 6, 12]
    print(f"1 -> {sol.listDivisors(1)}")  # [1]
    print(f"9474 -> {sol.listDivisors(9474)}")  # [1, 2, 3, 4, 6, 12]
    print(f"1 -> {sol.listDivisors(1)}")  # [1]