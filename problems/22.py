"""
Generate Parentheses

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.
"""

def generateParenthesis(self, n: int) -> List[str]:
    res = []

    def backtrack(currPara: list[str], opening_para_count: int, closing_para_count: int):
        # Our Goal
        if len(currPara) == (2 * n):
            res.append(''.join(currPara))
            return

        # Our choices
        if opening_para_count < n:
            currPara.append('(')
            backtrack(currPara, opening_para_count + 1, closing_para_count)
            currPara.pop()

        if closing_para_count < opening_para_count:
            currPara.append(')')
            backtrack(currPara, opening_para_count, closing_para_count + 1)
            currPara.pop()           


    backtrack([], 0, 0)

    return res
