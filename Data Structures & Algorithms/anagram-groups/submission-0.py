class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # dicts -> string lists

        for word in strs: # it through strings
            counts = [0] * 26
            for c in word: # it thru chars
                counts[ord(c) - ord('a')] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())
