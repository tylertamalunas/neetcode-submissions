class Solution:
    def trap(self, height: List[int]) -> int:
        # start at left and right, 2 max heights, left and right
        # checks if current point is lower than the minimum hieght between the max's
        #   if so, adds differece in min number and current num

        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        area = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                area += maxLeft - height[l] 
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                area += maxRight - height[r]
        return area
