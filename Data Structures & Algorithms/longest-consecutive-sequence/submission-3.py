class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to a set to remove duplicates and O(1) lookups
        # only focus on numbers where num-1 isnt in the set
        # use a max variable to store all time high, and a length var to store current run

        nset = set(nums)
        longest = 0

        for n in nset:
            if n - 1 not in nset:
                length = 1
                while n + length in nset:
                    length += 1
                longest = max(longest, length)
                
        return longest