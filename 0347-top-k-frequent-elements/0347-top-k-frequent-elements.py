class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        topKCounter = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
        
        for i in range(k):
            res.append(topKCounter[i][0])
        return res