"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents 
an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents 
the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

# TIME: O(n) Space: O(n)
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            opd2 = stack.pop()
            opd1 = stack.pop()
            val = int(eval(f"{opd1} {token} {opd2}"))
            stack.append(val)
        else:
            stack.append(token)
    return int(stack[0])
