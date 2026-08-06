class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort each and then check if equal

        if sorted(s) == sorted(t):
            return True
        else:
            return False