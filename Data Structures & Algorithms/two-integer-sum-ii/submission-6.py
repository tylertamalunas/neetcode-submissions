class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # is sorted low-> high
        # starts at index 1 (not 0) for answer
        # both add to target and first index must be lower than 2nd 
        #   2 pointers, l and r
        # if sum is over target, decrease right
        # if sum is under, increase left

        l = 0
        r = len(numbers) - 1

        while l < r:
            diff = numbers[l] + numbers[r]
            if diff == target:
                return [l+1, r+1]
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            
        return []