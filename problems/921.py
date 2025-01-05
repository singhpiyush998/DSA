"""
Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

You are given a parentheses string s.
In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))",
you can insert an opening parenthesis to be "(()))"
or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid
"""

"""
We could use a stack solution but its not really required,
generally we use stack when we have to keep track of a
element's value and its order, since this problem only
has () as value, we don't need to keep track of order
2 variables are enough
"""
def minAddToMakeValid(s: str) -> int:
    noOfUnclosedOpenPar = 0
    noOfUnclosedClosingPar = 0

    for c in s:
        if c == "(":
            noOfUnclosedOpenPar += 1
        else:
            if noOfUnclosedOpenPar > 0:
                noOfUnclosedOpenPar -= 1
            else:
                noOfUnclosedClosingPar += 1

    return noOfUnclosedOpenPar + noOfUnclosedClosingPar
