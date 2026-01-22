Quick note: in many number problems, applying modulo (%) lets you peel off specific digits or remainders to extract parts of the number efficiently.

Example with n = 5873 (modulo + integer division):
- Count digits
  - Pseudo: `count = 0; while n > 0: n = n/10; count++`
- Reverse number
  - Pseudo: `rev = 0; while n > 0: digit = n%10; rev = rev*10 + digit; n = n/10`
- Palindrome check
  - Pseudo: compute `rev` as above, then `isPalindrome = (rev == original)`
- Armstrong (sum of digits^k where k = digit count)
  - Pseudo: `k = digits(original); sum = 0; n = original; while n > 0: digit = n%10; sum += digit^k; n = n/10; isArmstrong = (sum == original)`
