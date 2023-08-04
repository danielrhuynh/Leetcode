class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Basically the idea here is regular binary search with edge cases for the left and             right sorted portions
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            # else keep searching
            if nums[mid] >= nums[low]:
                # We know the pivot put smaller numbers to the left
                if target > nums[mid] or target < nums[low]:
                    # If the target is greater than mid because things to the left
                    # of mid are lower we know the target is not there so set low to mid+1
                    # or if the target is less than low, since the array is pivoted it has to
                    # be in the right side
                    low = mid+1
                else:
                    # Else we know its in the left side
                    high = mid-1
            else:
                if target < nums[mid] or target > nums[high]:
                    # Same intuition here we know its in the left side
                    high = mid-1
                else:
                    # Here it is in the right side
                    low = mid+1
        return -1