class Solution {
public:
    void HeapDown(int index, int size, vector<int>& nums) {
        if (2*index+1 >= size) return;
        
        int leftChild = 2*index+1;
        int rightChild = 2*index+2;
        int chosenChild;
        if (leftChild < size && nums[leftChild] <= nums[rightChild]) chosenChild = leftChild;
        if (rightChild < size && nums[rightChild] <= nums[chosenChild]) chosenChild = rightChild;
                
        if (nums[chosenChild] < nums[index]) {
            swap(nums[chosenChild], nums[index]);
            HeapDown(chosenChild, size, nums);
        }
        else return;
    }
    int Dequeue(vector<int>& nums, int size) {
        if (size == 0) return -999;
        int res = nums[0];
        nums[0] = nums[size-1];
        HeapDown(0, size, nums);
        return res;
    }
    void sortColors(vector<int>& nums) {
        int size = 0;
        vector<int> res;
        for (int i = nums.size()-1; i >= 0; i--) {
            HeapDown(i, nums.size(), nums);
            size++;
        }
        for (int i = 0; i < size+i; i++) {
            res.push_back(Dequeue(nums,size));
            size--;
        }
        nums = res;
    }
};