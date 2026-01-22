class Solution:
    def reverse(self, x: int) -> int:
        """
        notes to future me (thought process + what tripped me up)

        core build rule (why rev = rev*10 + digit exists):
        - appending a digit to the end of a base-10 number means:
          "shift left one place" (multiply by 10) then "drop the new digit" (add digit).
          example: 32 -> 320 -> 321

        digit extraction rule:
        - last digit = x % 10
        - remove last digit = x // 10

        biggest pitfall i hit (python-specific):
        - in python, '^' is XOR, not exponent. use '**' for powers.
        - python negative modulo/division behave differently than truncation:
          -123 % 10 == 7 and -1 // 10 == -1 (can cause wrong digits or infinite loop).
          fix: separate sign and run the loop on abs(x) so %10 and //10 behave as expected.

        overflow insight (the real interview point):
        - overflow can happen while doing: rev = rev*10 + digit
        - we must check BEFORE multiplying by 10, because we are not allowed to "build it then check"
          with a larger integer type.
        - think of INT_MAX as a fence. when rev is close to the fence:
          case A) rev > INT_MAX//10  -> multiplying by 10 will definitely overflow
          case B) rev == INT_MAX//10 -> the next digit decides; it must be <= INT_MAX%10
        memory hook: "prefix protects multiply, last digit protects add"

        edge reminders:
        - leading zeros vanish automatically (120 -> 21) because integer math drops them.
        - apply sign at the end.
        - final bounds check is cheap and keeps the code safe/readable.

        complexity:
        - time: O(d) where d is number of digits (<= 10 for 32-bit)
        - space: O(1)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        MAX_PREFIX = INT_MAX // 10
        MAX_LAST = INT_MAX % 10

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10

            if rev > MAX_PREFIX:
                return 0
            if rev == MAX_PREFIX and digit > MAX_LAST:
                return 0

            rev = rev * 10 + digit

        rev *= sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev