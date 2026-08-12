class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # want to find the max number between the indices.
        # lower number is the max water that can be stored
        # take the lower number and multiply it by the number of indices between + 1
        # 2 pointer

        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            size = (r - l) * min(heights[l],heights[r])
            maxWater = max(maxWater, size)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater