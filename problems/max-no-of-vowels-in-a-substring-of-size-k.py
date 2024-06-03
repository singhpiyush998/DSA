def isVowel(c):
    return c in ("a", "e", "i", "o", "u")


def findMaxVowels(s: str, k: int) -> int:
    # Returns the maximum number of vowels in a substring of length k
    vowelCount = sum(isVowel(c) for c in s[:k])
    maxVowelCount = vowelCount
    for i in range(1, len(s) - k + 1):
        vowelCount = vowelCount - isVowel(s[i - 1]) + isVowel(s[i + k - 1])
        maxVowelCount = max(vowelCount, maxVowelCount)

    return maxVowelCount


"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
b a c a c b e f a o b  e  a  c  f  e
"""
s = "bacacbefaobeacfe"
k = 5

print(f"Number of vowels in a substring of size {
      k} in {s} is: {findMaxVowels(s, k)}")
