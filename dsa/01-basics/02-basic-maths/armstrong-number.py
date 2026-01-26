"""
Problem Statement:
https://leetcode.com/problems/armstrong-number/
"""
Given an integer n, return true if it is an Armstrong number, or false otherwise.

An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

Example 1:
Input: n = 153
Output: true
"""
Example 2:
Input: n = 123
Output: false
"""
Example 3:
Input: n = 1234
Output: false
"""
"""
class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        sum = 0
        original = n
        while n > 0:
            digit = n % 10
            sum += digit ** k
            n = n // 10
        return sum == original