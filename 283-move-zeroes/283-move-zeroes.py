class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bubble non zeros to the front instead of moving zeros to the end.
        low = 0
        high = 1
        
        while high < len(nums):
            if nums[high] != 0 and nums[low] == 0:
                nums[low], nums[high] = nums[high], nums[low]
                high +=1
                low +=1
            elif nums[high] == 0 and nums[low] == 0:
                high +=1
            else:
                high+=1
                low+=1