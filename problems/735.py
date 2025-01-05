"""
Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet
"""

def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []

    # if prev is +ve and curr is -ve then collison, otherwise no collison
    for a in asteroids:
        while stack and stack[-1] > 0 and a < 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                stack.pop()
                a = 0

        if a: stack.append(a)

    return stack
