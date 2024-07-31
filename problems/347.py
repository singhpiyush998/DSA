"""
Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.
"""

# Time: O(n) Space: O(n)
def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    freq = [[] for _ in range(len(nums) + 1)] # index-count and value-items which are "count" many times
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
