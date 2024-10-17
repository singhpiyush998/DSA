"""
Group Anagrams

Given an array of strings strs, group the anagrams
together. You can return the answer in any order
"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return anagram_map.values()
