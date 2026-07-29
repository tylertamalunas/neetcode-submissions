class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # SORTED!!! low to high
        # 1 indexed
        # index 1 < 2
        # 2 pointer
        #   if sum > target, decrease right
        #   if sum < target, increase left

        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            elif sum == target:
                return [l+1, r+1]
                
