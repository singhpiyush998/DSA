"""
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order
"""

def findAnagrams(s: str, p: str) -> list[int]:
    freq_p = {}

    for c in p:
        freq_p[c] = 1 + freq_p.get(c, 0)

    l = 0
    freq_s = {}

    res = []
    for r in range(len(s)):
        freq_s[s[r]] = 1 + freq_s.get(s[r], 0)

        if (r - l + 1) == len(p):      
            if freq_s == freq_p:
                res.append(l)

            freq_s[s[l]] -= 1
            if freq_s[s[l]] == 0:
                del freq_s[s[l]]
            l += 1
        
    return res
