"""
LeetCode Problem: Palindrome Number (#9) (easy)
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if x < 0:
            return False
        while temp != 0:
            number = temp % 10
            rev = (rev * 10) + number
            temp = temp // 10
        if x == rev:
            return True
        else:
            return False
        

"""
Explanation:
To determine if an int is a palindrome, we compare the reversed integer to the original.
We first check if the integer is negative; if so, we return False since negative numbers cannot be palindromes.
We then reverse the int using a while loop that extracts each digit and constructs the reversed number.
Finally, we compare the reversed integer to the original integer and return True if they are the same
"""

