"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters
"""


def lengthOfLongestSubstring(s: str) -> int:
    uniqueChars = set()
    maxSubStrSize = l = 0

    for r in range(len(s)):
        while s[r] in uniqueChars:
            uniqueChars.remove(s[l])
            l += 1

        uniqueChars.add(s[r])
        maxSubStrSize = max(maxSubStrSize, r - l + 1)

    return maxSubStrSize


print(f"Longest substring without repeating characters in abcabcbb is {
      lengthOfLongestSubstring('abcabcbb')}")

print(f"Longest substring without repeating characters in bbbbb is {
      lengthOfLongestSubstring('bbbbb')}")

print(f"Longest substring without repeating characters in pwwkew is {
      lengthOfLongestSubstring('pwwkew')}")


print(f"Longest substring without repeating characters in ynyo is {
      lengthOfLongestSubstring('ynyo')}")
