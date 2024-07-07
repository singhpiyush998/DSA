"""
Valid Parentheses

Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1.    Open brackets must be closed by the same type of brackets.
2.    Open brackets must be closed in the correct order.
3.    Every close bracket has a corresponding open bracket of the same type.
"""

# Time: O(n) Space: O(n)
def isValid(s: str) -> bool:
    stack = []
    map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for c in s:
        if c in map:
            if len(stack) == 0 or map[c] != stack.pop():
                return False
        else:
            stack.append(c)

    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("["))
print(isValid("]"))
