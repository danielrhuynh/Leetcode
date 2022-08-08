class Solution {
public:
    void sortColors(vector<int>& nums) {
        int sizeArray = nums.size();
        for (int i = 0; i < sizeArray; i++) {
            for (int j = 0; j < sizeArray-1; j++) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
    }
};