# Write a function to find the
# longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    for i in range(min(len(s) for s in strs)):
        if len({s[i] for s in strs}) != 1:
            break
        res += strs[0][i]
    
    return res

print(longestCommonPrefix(["flower","flower","flower","flower"]))
