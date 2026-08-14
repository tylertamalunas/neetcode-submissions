class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # move r along until a different letter is found, then add to a counter. Once counter == k+1, set teh length to the max of current and 
        # previous length. 
        # but how to do for next letter
        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # add 1 to existing value, or create k:v pair
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)

        return res