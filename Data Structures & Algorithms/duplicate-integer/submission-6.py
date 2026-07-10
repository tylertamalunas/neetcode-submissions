class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set, if size is not the same as original return false, else true
        result = []
        for num in nums:
            if num in result:
                return True
            else:
                result.append(num)
        return False
