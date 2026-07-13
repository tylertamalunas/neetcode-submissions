class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort method
        # map the counts
        # iterate through k,v and sort into buckets
        # start from last bucket and add items to answer until there are k values

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n,c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

