class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # True if same letters and amount of letters 
        # sort and then double for loop
        # array of 26 letters 

        new_s = sorted(s)
        new_t = sorted(t)

        if new_s == new_t:
            return True
        else:
            return False