"""
Daily Temperatures
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there
is no future day for which this is possible, keep answer[i] == 0 instead.
"""

# Space: O(n) Time: O(n)
# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     answer = [0] * len(temperatures)
#     stack = [] # pair: (temperature, index)
#     for i in range(len(temperatures) - 1, -1, -1):
#         while stack and temperatures[i] >= stack[-1][0] :
#             stack.pop()
#         if stack: answer[i] = (stack[-1][1] - i)
#         stack.append((temperatures[i], i))

# Space: O(n) Time: O(n)
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            topI = stack.pop()
            answer[topI] = i - topI
        stack.append(i)

    return answer
