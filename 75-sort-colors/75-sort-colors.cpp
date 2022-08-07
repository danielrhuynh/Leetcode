class Solution {
public:
    void sortColors(vector<int>& nums) {
        int sizeNums = size(nums);
        if (sizeNums < 2) return;
        for (int i = 0; i <= sizeNums-1; ++i) {
            for (int j = 0; j <= sizeNums-2; ++j) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
    }
};