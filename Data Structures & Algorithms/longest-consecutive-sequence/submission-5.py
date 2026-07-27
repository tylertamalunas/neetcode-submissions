class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to hash set.
        # only need to look at starting numbers with no n-1 in list

        nset = set(nums)
        longest = 0

        for num in nset:
            length = 1
            if num - 1 not in nset:
                while num + length in nset:
                    length += 1
                longest = max(longest, length)
        return longest