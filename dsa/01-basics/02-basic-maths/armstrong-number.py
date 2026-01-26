"""
Problem Statement:
https://leetcode.com/problems/armstrong-number/

Given an integer n, return true if it is an Armstrong number, or false otherwise.

An Armstrong number is a number that is the sum of its own digits each raised
to the power of the number of digits.

Example 1:
Input: n = 153
Output: true

Example 2:
Input: n = 123
Output: false

Example 3:
Input: n = 1234
Output: false
"""

from math import log10


class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n <= 0:
            return n == 0  # 0 is technically armstrong
        k = int(log10(n) + 1)
        sum = 0
        original = n
        while n > 0:
            digit = n % 10
            sum += digit ** k
            n = n // 10
        return sum == original


# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Test cases
    print(f"153 -> {sol.isArmstrong(153)}")  # True (1³ + 5³ + 3³ = 153)
    print(f"123 -> {sol.isArmstrong(123)}")  # False
    print(f"9474 -> {sol.isArmstrong(9474)}")  # True (9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
    print(f"1 -> {sol.isArmstrong(1)}")  # True
