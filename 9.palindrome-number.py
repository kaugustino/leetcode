#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.07%)
# Likes:    12732
# Dislikes: 2739
# Total Accepted:    5M
# Total Submissions: 8.7M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]

        # Solution without str manipulation
        # O(log n)
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0 and x != 0:
            return False

        reverse = 0
        # Stop when reverse now has greater number of digits
        # Only go halfway
        while x > reverse:
            # Shifting over the last digits in x
            # when multiplying by 10
            reverse = (reverse * 10) + (x % 10)
            # Chop off the last digit in x
            x = x // 10

        # For odd digit length
        return x == reverse or x == reverse // 10

# @lc code=end

