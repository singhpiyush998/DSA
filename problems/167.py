"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
"""

def twoSum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        val = numbers[i] + numbers[j]
        if val == target:
            break
        elif val > target:
            j -= 1
        else:
            i += 1
        
    return [i + 1, j + 1]

print(twoSum([5,25,75], 100))
print(twoSum([2, 3, 4], 6))
print(twoSum([2,7,11,15], 9))
print(twoSum([-1 , 0], -1))
