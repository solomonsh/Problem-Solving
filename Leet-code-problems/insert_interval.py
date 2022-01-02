class Solution:
    def shares_interval(self,interval1,interval2):
        if interval1[1]<interval2[0] or interval2[1]<interval1[0]:
            return False
        else:
            return True
    def insert(self, intervals, newInterval):

        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        merged = []
        result = []
        for i,interval in enumerate(intervals):
            if self.shares_interval(interval,newInterval):
                merged.append(interval[0])
                merged.append(interval[1])
                merged.append(newInterval[0])
                merged.append(newInterval[1])
            else:
                result.append(interval)

        merged.sort()
        if len(merged)>0:
            result.append([merged[0],merged[-1]])
        else:
            result.append(newInterval)
        result.sort()
        return result
        

sol = Solution()

 
# print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])==[[1, 2], [3, 10], [12, 16]])

# print(sol.insert([[1,3],[6,9]],[2,5])==[[1, 5], [6, 9]])
# print(sol.insert([],[5,7])==[[5,7]])

# print(sol.insert([[1,5]],[2,3])==[[1,5]])

# print(sol.insert([[1,5]],[2,7]) ==[[1,7]])
# print(sol.insert([[1, 5]], [6, 8])==[[1,5],[6,8]])


print(sol.insert([[1,5]], [0,0])==[[0,0],[1,5]])

print(sol.insert([[2, 4], [5, 7], [8, 10], [11, 13]], [3, 6])==[[2,7],[8,10],[11,13]])

print(sol.insert([[0,2],[3,9]], [6,8])==[[0,2],[3,9]])  


print(sol.insert([[1,5],[6,9]], [2,5])==[[1,5],[6,9]])
print(sol.insert([[3,5],[12,15]], [6,6])==[[3,5],[6,6],[12,15]])
 