class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True
        return False