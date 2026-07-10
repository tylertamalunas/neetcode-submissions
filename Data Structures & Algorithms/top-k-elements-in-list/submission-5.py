class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        0. create a hashmap and list of lists
        1. map the counts of each number
        2. sort those counts into buckets 
        3. go thorugh buckets in reverse to find top k most frequent
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n,c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans