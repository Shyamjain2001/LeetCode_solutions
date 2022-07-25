class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # example: 
        # [1,3], [2,6], [5, 10]
        # [1,6] [5,10]
        # [1,10]
        
        if len(intervals) == 1:
            return [intervals[0]] 
        
        intervals.sort(key=lambda item: item[0]) # [1,3], [2,6], [5, 10]
        
        output = [intervals[0]] # [1,3]
        max_val = 0
        
        
        for i in range(1, len(intervals)):
            cur = intervals[i] # [2,6], [5,10]
            
            # [1,3]
            # [1,6]
            if(output[-1][1] >= cur[0]): # overlapping
                max_val = max(output[-1][1], cur[1]) # 3 vs 6, 6 vs 5
                output[-1][1] = max_val # [1,6], [1,10]
            else: 
                output.append(cur) 
        return output # [1,10]