class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map count of items, then sort into buckets

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # map
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # add to freq 
        for n,c in count.items():
            freq[c].append(n)

        
        # find top k
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans