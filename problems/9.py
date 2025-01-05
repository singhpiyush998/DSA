"""
Palindrome Number

Given an integer x, return true if x is a
palindrome, and false otherwise.
"""

def isPalindrome(x: int) -> bool:
    st = str(x)
    for i in range(len(st) // 2):
        if st[i] != st[~i]:
            return False
    return True

print(isPalindrome(121))
