class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Store count in hashmap
        seen = Counter(nums)
        return max(seen, key=lambda x: seen[x])
        