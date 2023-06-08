class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [height[0]]
        max_r = [height[-1]]
        min_l_r = []
        res = 0
        
        for i in range(1, len(height)):
            max_l.append(max(height[i], max_l[-1]))
        for i in range(len(height)-2, -1, -1):
            max_r.append(max(height[i], max_r[-1]))
        for i in range(len(height)):
            min_l_r.append(min(max_l[i], max_r[len(height)-1-i]))
                                     
        # Formula for water contained = min(l,r) - height[i]
        for i in range(len(height)):
            val = max((min_l_r[i] - height[i]), 0)
            res += val
        return res
                                
        
            
            
            
        