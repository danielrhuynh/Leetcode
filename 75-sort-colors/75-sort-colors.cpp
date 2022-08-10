class Solution {
public:
    void selectionSort(vector<int>& nums, int start) {
        // Base case
        if (nums.size()-1 == start || nums.size() == 1) {
            return;
        }
        int minIndex = start;
        for (int i = start; i < nums.size(); i++) {
            if (nums[i] < nums[minIndex]) {
                    minIndex = i;
                }
            }
        swap(nums[start], nums[minIndex]);
        selectionSort(nums, start+1);
    }
    void sortColors(vector<int>& nums) {
        selectionSort(nums, 0);
    }
};