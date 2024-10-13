class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        res = []
        # We can get time savings by slicing to the top k elements in the list!
        for key, val in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]:
            res.append(key)
        return res