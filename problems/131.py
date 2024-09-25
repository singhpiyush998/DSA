"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.
"""

def partition(self, s: str) -> List[List[str]]:
    res = []

    def isValidPalindrome(p):
        i, j = 0, len(p) - 1
        while i < j:
            if p[i] != p[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def backtrack(partitionIndex, currPartitions):
        # Our Goal
        if partitionIndex == len(s):
            res.append(currPartitions.copy())

        # Our Choices
        for i in range(partitionIndex, len(s)):
            partition = s[partitionIndex : i + 1]

            # Our Constraint
            if not isValidPalindrome(partition):
                continue

            currPartitions.append(partition)
            backtrack(i + 1, currPartitions)
            currPartitions.pop()

    backtrack(0, [])
    
    return res
