"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses 
some pile of bananas and eats k bananas from that pile. If the pile has less than
k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = max(piles)

    while l <= r:
        speed = (r + l) // 2
        canEatAll = True

        hour = 0
        for pile in piles:
            hour += ceil(pile / speed)

        if hour <= h:
            res = min(res, speed)
            r = speed - 1
        else:
            l = speed + 1

    return res
