class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map with the values being a list
        # how do i find similar string? sort word and use as key? O(nlogm)
        strs_map = defaultdict(list)

        for s in strs:
            keys = [0] * 26
            for l in s:
                keys[ord(l) - ord('a')] += 1
            strs_map[tuple(keys)].append(s)
        
        return list(strs_map.values())