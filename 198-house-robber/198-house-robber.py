class Solution:
    def rob(self, nums: List[int]) -> int:
        arrayNotAdj, arrayNotCurr = 0, 0
        
        for curr in nums:
            higher = max(curr+arrayNotAdj, arrayNotCurr)
            arrayNotAdj = arrayNotCurr
            arrayNotCurr = higher
        moreMoney = max(arrayNotAdj,arrayNotCurr)
        return moreMoney
        