class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums)+1)] # With one additional one to account for the zero
        
        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        for n, c in cnt.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            