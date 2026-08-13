class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set l and r at same spot. Increase r until a duplicate is found, then increase l until duplicates are gone. 
        maxLength = 0
        l = 0
        current = ""
        for r in range(len(s)):
            while s[r] in current:
                l += 1
                current = s[l:r]
            current = s[l:r+1]
            maxLength = max(maxLength, len(current))
        return maxLength