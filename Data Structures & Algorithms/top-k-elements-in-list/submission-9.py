class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map counts, then bucket sort, then reverse look through array till k items found
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