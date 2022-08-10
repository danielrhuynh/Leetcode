class Solution {
public:
    void sortColors(vector<int>& nums) {
        bool flag = false;
        do {
            flag = false;
            for (int i = 0; i < nums.size()-1; i++) {
                if (nums[i] > nums[i+1]) {
                    swap(nums[i], nums[i+1]);
                    flag = true;
                }
            }
        }
        while (flag);
    }
};