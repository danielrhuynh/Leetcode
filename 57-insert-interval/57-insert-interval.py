class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = 0
        e = 0
        res = []
        
        for i in range(len(intervals)):
            # If new interval goes before intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If new interval goes after intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Else overlaps
            else:
                newStart = min(intervals[i][0], newInterval[0])
                newEnd = max(intervals[i][1], newInterval[1])
                newInterval = [newStart, newEnd]
        
        res.append(newInterval)
        
        return res