# def plusOne(self, digits: List[int]) -> List[int]:
#     res = []
#     carry = 1
#     i = -1
#     for i in digits[::-1]:
#         num = i + carry 
#         carry = num // 10
#         val = num % 10
#         res = [val, *res]
#
#     if carry == 1:
#         res.insert(0, 1)
#     return res

def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1, *digits]

print(plusOne([1, 9, 5]))
