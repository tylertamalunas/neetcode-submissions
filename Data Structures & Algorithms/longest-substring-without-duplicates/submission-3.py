class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, use a hash map to keep track of index locations for faster jumping of left pointer when a duplicate is found. 
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

