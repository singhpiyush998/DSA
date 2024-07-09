"""
Car Fleet

There are n cars at given miles away from the starting mile 0,
traveling to reach the mile target.

You are given two integer array position and speed, both of length n,
where position[i] is the starting mile of the ith car and 
speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and 
then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. 
The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, 
it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.
"""

# The speed of fleet is the speed of slowest car in the fleet
# Time: O(n) Space: O(n)
# def carFleet(target: int, position: list[int], speed: list[int]) -> int:
#     stack = []
#
#     for p, s in sorted((zip(position, speed)), reverse=True):
#         stack.append((target - p) / s)
#         if len(stack) >= 2 and stack[-1] <= stack[-2]:
#             stack.pop()
#
#     return len(stack)

# Time: O(n) Space: O(1)
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    fleets = currFleetTravelTime = 0
    for p, s in sorted((zip(position, speed)), reverse=True):
        currCarTravelTime = (target - p) / s
        if currFleetTravelTime < currCarTravelTime:
            fleets += 1
            currFleetTravelTime = currCarTravelTime

    return fleets

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(carFleet(10, [3], [3]))
print(carFleet(100, [0,2,4], [4,2,1]))
