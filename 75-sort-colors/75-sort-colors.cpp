class Solution {
public:
    void bubbleSort(vector<int>&nums, int n) {
        if (n == 1) {
            return;
        }
        for (int i = 0; i < n-1; i++) {
            if (nums[i] > nums[i+1]) {
                swap(nums[i], nums[i+1]);
            }
        }
        if (n-1 < 1) {
                return;
            }
        bubbleSort(nums, n-1);
    }
    void sortColors(vector<int>& nums) {
        bubbleSort(nums, nums.size());
    }
};