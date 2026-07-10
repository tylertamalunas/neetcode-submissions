class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through each word in list, then sort that words letters and check if it exists inside the hashmap.
        # if it does, append the original word to that key (sorted word) value {key, [words]}
        # if not, add the k,v pair to the hashmap
        # once done, return the values in the hashmap as a list [[values1], [values2], [etc]]

        hmap = {}
        for word in strs:
            sword = str.join("", sorted(word))
            if sword in hmap.keys():
                hmap[sword].append(word)
            else:
                hmap[sword] = [word]
        answer = []
        for v in hmap.values():
            answer.append(v)
        return answer