class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # must be 3 seperate indexes
        # all add to 0
        # no duplicate combos (i.e [0, 1, -1], [-1, 0, 1])
        # can sort
        # return empty array if no answer

        # since list is sorted, can check if answer already contains combo
        #

        nums.sort()
        ans = []
        

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                if threeSum == 0:
                    if [a, nums[l], nums[r]] not in ans:
                        ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
        return ans

        #fix the leftmost number (i)
            # if its 0, then break
        # l is after i and r is at the end
        #if sum > 0 decrease r, if sum < 0 increse l
        # if sum = 0 check for duplicates and record. move i by 1
