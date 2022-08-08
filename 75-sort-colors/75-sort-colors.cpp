class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Using selection sort
        int sizeArray = nums.size();
        for (int i = 0; i < sizeArray-1; i++) {
            int minIndex = i;
            // find min value
            for (int j = i+1; j < sizeArray; j++) {
                if (nums[j] < nums[minIndex]) {
                    minIndex = j;
                }
            }
            // Perform swap
            swap(nums[i], nums[minIndex]);
        }
    }
};