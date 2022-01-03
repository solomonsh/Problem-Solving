 
class Solution:
    def overlaps(self,interval1,interval2):
        if interval1[1]<interval2[0] or interval2[1]<interval1[0]:
            return False
        else:
            return True
    
    def merge(self, intervals): 
       
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

        
     


sol = Solution()

print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))

 
        
