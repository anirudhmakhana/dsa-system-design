from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   # Write your code here.
   count = 0
   while n > 0:
      n = n // 10
      count += 1
   return count


# log10(n) + 1
def countDigit(n: int) -> int:
   return int(log10(n) + 1)