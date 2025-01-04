"""
Backspace String Compare

Given two strings s and t,
return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

def backspaceCompare(s: str, t: str) -> bool:
    def getNextValidIndex(string, index):
        backspace = 0
        while index >= 0:
            if backspace == 0 and string[index] != "#":
                break
            elif string[index] == "#":
                backspace += 1
            else:
                backspace -= 1
            index -= 1

        return index

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = getNextValidIndex(s, i)
        j = getNextValidIndex(t, j)

        char_s = s[i] if i >= 0 else ""
        char_t = t[j] if j >= 0 else ""
        if char_s != char_t:
            return False

        i, j = i - 1, j - 1

    return True
