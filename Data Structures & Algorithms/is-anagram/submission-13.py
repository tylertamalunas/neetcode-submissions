class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort each and then check if equal
        ss = sorted(s)
        tt = sorted(t)

        if ss == tt:
            return True
        else:
            return False