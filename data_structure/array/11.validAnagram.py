"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def validAnagram(s, t):
    """
    Time: O(nlogn)
    input: length of 2 str
    output: what if 2 a empty, None
        for each character in s: sorted_s
        for each character in t: sorted_t
        return sorted_s == sorted_t
    """

s = "anagram" 
t = "nagaram"
validAnagram(s, t)
