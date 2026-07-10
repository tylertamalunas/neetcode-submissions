class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input 2 strings
        # output true false
        # process = check if there is the same amount of letters in each string
        # setup 2 array or map with a count of how many of each letter is in each string
        # then check if each map/array is the same

        if len(s) != len(t):
            return False     

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            # {r : 1 + ((current value) or (0 if doesnt exist yet)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countT == countS