# def passThePillow(n: int, time: int) -> int:
#     direction = -1
#     i = 1
#     while time:
#         if i % n == 0 or i == 1:
#             direction *= -1
#         i += direction
#         time -= 1
#     return i
        
def passThePillow(n: int, time: int) -> int:
    rounds = time // (n - 1)
    k = time % (n - 1)
    return k + 1 if rounds % 2 == 0 else n - k
    

print(passThePillow(3, 2))