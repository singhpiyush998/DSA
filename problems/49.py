"""
Group Anagrams

Given an array of strings strs, group the anagrams
together. You can return the answer in any order
"""

from collections import defaultdict

# def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#     dt = defaultdict(list)

#     for s in strs:
#         charCount = [0] * 26
#         for c in s:
#             charCount[ord(c) - ord('a')] += 1
#         dt[tuple(charCount)].append(s)

#     return dt.values()

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return anagram_map.values()
