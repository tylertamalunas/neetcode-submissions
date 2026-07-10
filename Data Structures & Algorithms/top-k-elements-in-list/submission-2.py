class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1) map the counts
            a) create hmap
            b) create array that is size of length of nums
            c) loop thru hmap and count nums 
        2) loop through key and values and place each value in the array, at the index for its count
        3) reverse loop through frequency array and add any numbers found to the answer array
        4. once answer array is the size of k, return it
        '''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n,c in count.items():
            freq[c].append(n)
            
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                