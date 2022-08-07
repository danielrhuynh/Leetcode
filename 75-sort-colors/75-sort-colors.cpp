class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (size(nums) < 2) return;
        for (int i = 0; i <= size(nums)-1; i++) {
            for (int j = 0; j <= size(nums)-2; j++) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
    }
};