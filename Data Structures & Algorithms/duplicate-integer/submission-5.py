class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set, if set contains num, return False

        ans_set = set(nums)

        if len(ans_set) < len(nums):
            return True
        else:
            return False