class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip whitespace (or skip past)
        # 2 pointer, one at start, the other at end. move closer until a mismatch. 
        # if they are the same index, return True. 

        l = 0
        r = len(s) - 1
        
        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
