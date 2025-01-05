"""
Longest Common Prefix

Write a function to find the
longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

# O(n^2)
# def longestCommonPrefix(strs: list[str]) -> str:
#     res = ""
#     for i in range(min(len(s) for s in strs)):
#         if len({s[i] for s in strs}) != 1:
#             break
#         res += strs[0][i]

#     return res

# O(n * logn)
def longestCommonPrefix(strs: list[str]) -> str:
    ans=""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first),len(last))):
        if(first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

print(longestCommonPrefix(["flower","flower","flower","flower"]))
