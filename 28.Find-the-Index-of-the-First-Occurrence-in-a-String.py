"""
28. Find the Index of the First Occurrence in a String
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack = haystack.lower()
        needle = needle.lower()        
        needle_length = len(needle)
        haystack_length = len(haystack)
        result = []

        for i in range(haystack_length):
            piece_of_hay = haystack[i:i+needle_length]

            if needle == piece_of_hay:
                result.append(i)

        if len(result) == 0:
            return -1
        if result[0] != -1:
            return result[0]
        

# i = Solution()
# print(i.strStr("hello","ll"))
