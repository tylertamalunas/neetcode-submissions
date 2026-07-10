class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set, if size is not the same as original return false, else true
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False