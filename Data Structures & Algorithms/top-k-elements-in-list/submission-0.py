class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash table where key=num and value=count. Gets counts of each number.
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        # need to find top k elements within the list. loop through and store max's
        answer = [0]
        num_counts = collections.Counter(nums)
        return heapq.nlargest(k,num_counts.keys(), key=num_counts.get)
        