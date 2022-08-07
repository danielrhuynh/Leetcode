class Solution {
public:
    void sortColors(vector<int>& nums) {
        int sizeNums = nums.size();
        if (sizeNums < 2) return;
        for (int i = 0; i <= sizeNums-1; ++i) {
            for (int j = 0; j <= sizeNums-2; ++j) {
                if (nums[j] > nums[j+1]) {
                    swap(nums[j], nums[j+1]);
                }
            }
        }
    }
};