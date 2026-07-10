class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input is array of strings
        # output is sublist of strings with anagrams in their own lists inside it
        # how to get there = group same length strings together, then make hashmap for each string with letter type and count
        #   then check which ones are equal, group equal ones together

        # whats this?
        res = defaultdict(list)

        # go through each string in strs
        for s in strs:
            # create letter array
            count = [0] * 26
            # go through each char in that string and add 1 to the array index that corresponds to the letter
            for c in s:
                count[ord(c) - ord('a')] += 1 # find the index for that letter c, count[88(b) - 87(a)]  = count[1] 
                                                # then add 1 to the value for that letters index, count[1] += 1
            # lists cant be keys, so need to change it into a tuple
            res[tuple(count)].append(s)
        return res.values()