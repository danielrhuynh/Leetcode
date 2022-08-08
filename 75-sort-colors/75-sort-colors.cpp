class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Using heap sort
        priority_queue <int> minHeap;
        for (int i = 0; i < nums.size(); i++)
            minHeap.push(nums[i]);
        for (int i = 0; i < nums.size(); i++) {
            nums[nums.size()-i-1] = minHeap.top();
            minHeap.pop();
        }
        
    }
};