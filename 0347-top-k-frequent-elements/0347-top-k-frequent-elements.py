class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        res = []
        
        for i in range(k):
            key = max(numsCounter, key=numsCounter.get)
            res.append(key)
            numsCounter[key] = 0
        return res
        