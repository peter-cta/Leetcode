"""Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0): 
            return False
        half = 0
        while x > half:
            half, x = half*10 + x%10,x//10
        return x in(half, half//10)

sl = Solution()
print(sl.isPalindrome(10))
    
