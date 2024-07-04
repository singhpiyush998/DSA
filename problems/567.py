"""
Permutation in String

Given two strings s1 and s2,
return true if s2 contains a permutation of s1, or false otherwise.
In other words, 
return true if one of s1's permutations is the substring of s2.
"""

from collections import Counter

# def checkInclusion(s1: str, s2: str) -> bool:
#     freq_s1 = Counter(s1)
#             return any(
#                 Counter(s2[l:l+len(s1)]) == freq_s1
#                 for l in range(len(s2) - len(s1) + 1)
#             )

# TIME: O(26.n) Space: O(n)
def checkInclusion(s1: str, s2: str) -> bool:
    freq_s1, freq_s2 = {}, {}

    for i in range(len(s1)):
        freq_s1[s1[i]] = 1 + freq_s1.get(s1[i], 0) 

    l = 0
    for r in range(len(s2)):
        freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)

        # O(26) ~ O(1) == constant time as s1 and s2 containes a-z only
        if freq_s2 == freq_s1:
            return True

        if (r - l + 1) == len(s1):
            freq_s2[s2[l]] -= 1
            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]
            l += 1
        
    return False

print(checkInclusion("adc", "dcda"))
print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboooo"))
