class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # cant be same index
        # index 1 < index 2 (the index or value?)
        # array is sorted in ascending order
        # sorted, so 2 pointer, one at each end coming together
        # if sum is larger than target, the right number cant be correct. Opposite for left
        

        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            elif sum < target:
                l += 1
            