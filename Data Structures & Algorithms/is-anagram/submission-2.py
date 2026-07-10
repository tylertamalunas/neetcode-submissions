class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input = 2 strings
        # output = true /false
        # how to get there = 2 hash maps, they count how many of each letter is in the word
        #           loop thru one string, value is key, 1 + value of key  is counter
        if len(s) != len(t):
            return False

        mapS = {}
        mapT = {}
        for i in range(len(s)):
            # key = letter at that index in string
           mapS[s[i]] = 1 + mapS.get(s[i], 0)
           mapT[t[i]] = 1 + mapT.get(t[i], 0)
        return mapT == mapS