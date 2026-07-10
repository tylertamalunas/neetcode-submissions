class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table. 
        # loop once with for loop, if target - index_val == past_number_in_hash_map
        #   return indice of current, and key of map value
        hm = []

        for num in range(len(nums)):
            val = target - nums[num]
            if val in hm:
                return [hm.index(val), num]
            else:
                hm.append(nums[num])
