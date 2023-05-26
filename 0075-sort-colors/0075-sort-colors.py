class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using heap sort
        def heapify(arr, n, i):
            # Set largest to be the root
            largest = i
            # These are how you select children in the list interpretation of a heap
            l = 2 * i + 1
            r = 2* i + 2
            
            # Check if left child or right child of root exists and is greater than the root
            if l < n and arr[largest] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            # If the largest is not the root (i) then we need to swap the root and heapify down
            if largest != i:
                # Swap values
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        def heap_sort(arr):
            # Put elements into the heap backwards and take them out
            for i in range(len(arr)//2-1, -1, -1):
                heapify(arr, len(arr), i)
            # Take elements out one by one from the back
            for i in range(len(arr)-1, 0, -1):
                # Swap front and back to 'take out'
                # This works since we put the largest value at the index -1 position
                # and then decrement i so we effectively cut that position for the heap
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
        heap_sort(nums)
            
            
                
            
        