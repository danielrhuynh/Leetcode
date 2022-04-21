class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        
        for i in range(k):
            high = -inf
            n = 0
            for key, val in freq.items():
                if val > high:
                    high = val
                    n = key
            res.append(n)
            freq.pop(n, None)
        return res