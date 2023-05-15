class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Store count in hashmap
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        return max(seen, key=lambda x: seen[x])
        