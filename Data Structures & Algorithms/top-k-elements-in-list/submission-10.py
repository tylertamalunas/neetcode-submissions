class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make array the size of nums
        # make a map to count 
        # go through the array in reverse until k values added to answer 

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
                
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans