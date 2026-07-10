class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in = str array
        # out = grouped anagrams
        # how = array of letters, map of letter combos with value as strings

        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            map[tuple(count)].append(s)
        
        return map.values()