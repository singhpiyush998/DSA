"""
A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring,
every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.


Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc",
"bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
"""


def countGoodSubstrings(s: str) -> int:
    goodSubStrCount = 0

    uniqueChars = set()
    l = 0
    for r in range(len(s)):
        while s[r] in uniqueChars:
            uniqueChars.remove(s[l])
            l += 1

        uniqueChars.add(s[r])
        if (r - l + 1) == 3:
            goodSubStrCount += 1
            uniqueChars.remove(s[l])
            l += 1

    return goodSubStrCount


print(countGoodSubstrings("owuxoelszb"))
print(countGoodSubstrings("xyzzaz"))
print(countGoodSubstrings("aababcabc"))
