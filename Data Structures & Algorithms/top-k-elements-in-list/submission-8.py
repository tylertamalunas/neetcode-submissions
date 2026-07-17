class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map the counts, create a bucket sort, reverse look thru bucet for k
        count = {} 
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n,c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans