class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        res = []
        
        while low <= high:
            # Using the knowledge that nums in non-descending
            if abs(nums[high]) > abs(nums[low]):
                res.append(nums[high]**2)
                high-=1
            else:
                res.append(nums[low]**2)
                low+=1
        # Array is sorted in descending order, reverse it
        return res[::-1]
                