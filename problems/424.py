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

"""
For a substring to be valid, we need window_length - maxf <= k. Here,
maxf is the frequency of the most common character in the current window.
The difference window_length - maxf tells us how many characters
we'd need to change to make the whole window the same character.

The biggest valid substring (answer) we can get is of size maxf + k. So,
the larger maxf is, the better. If maxf doesn't change or goes down,
our potential best answer doesn't change. We don't need to update maxf in this case.

On the other hand, if maxf goes up, it means we've found a character in the
current window that appears more often than in previous windows.
This means we might be able to get a longer valid substring, so we update maxf.
"""
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
