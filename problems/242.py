from itertools import zip_longest
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    count = defaultdict(int)
    for i, j in zip_longest(s, t):
        count[i] += 1
        count[j] -= 1

    return all(not i for i in count.values())

print(isAnagram("a", "ab"))
# print(isAnagram("anagram", "nagaram"))
