from collections import defaultdict

def topKFrequent(nums, k):
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    freq = [[] for _ in range(len(nums) + 1)]
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res
