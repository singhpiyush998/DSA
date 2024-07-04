"""
Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

"""

# TIME: O(26.n), where there are 26 alphabets in english
def characterReplacement(s: str, k: int) -> int:
    res = 1
    freq = {}

    l = 0
    for r in range(len(s)):
        freq[s[r]] = 1 + freq.get(s[r], 0)

        # number of replacements needed = length of window - count of most frequent element
        while (r - l + 1) - max(freq.values()) > k:
            freq[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res

# TIME: O(n)
# def characterReplacement(s: str, k: int) -> int:
#     res = 1
#     freq = {}
#
#     maxf = 0
#     l = 0
#     for r in range(len(s)):
#         freq[s[r]] = 1 + freq.get(s[r], 0)
#         maxf = max(maxf, freq[s[r]])
#
#         # number of replacements needed = length of window - count of most frequent element
#         while (r - l + 1) - maxf > k:
#             freq[s[l]] -= 1
#             l += 1
#
#         res = max(res, r - l + 1)
#
#     return res


print(characterReplacement("ABABBA", 2))
print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
