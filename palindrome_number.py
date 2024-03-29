# -*- coding: utf-8 -*-
"""
Example 1:

Input: 121
Output: true


Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up:

Coud you solve it without converting the integer to a string?
"""

import reverse_digits as rg

def palindrome_num(number):
    palindrome = False
    if number == rg.sign_reverse_digits(number):
        palindrome = True
    print(palindrome)

def palindrome_in_one_line(numb):
    return False if numb < 0 else numb == int(str(numb)[::-1])

palindrome_num(1231)
palindrome_num(121)
palindrome_num(16861)

print(palindrome_in_one_line(-11))
print(palindrome_in_one_line(911))
print(palindrome_in_one_line(9119))