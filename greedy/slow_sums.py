# def getTotalTime(lst):
#     lst.sort() #n * log n

#     penalities = 0
#     while len(lst)>1:
#         sums = lst[-2]+lst[-1]
#         penalities+=sums
#         lst.pop()
#         lst.pop()
#         lst.append(sums)
#     return penalities



import heapq
def getTotalTime(lst):
    lst = [-1*i for i in lst]

    heapq.heapify(lst) 
    penalities = 0
    while len(lst)>1:
        sums =  heapq.heappop(lst)
        sums += heapq.heappop(lst)
        penalities+=sums
        heapq.heappush(lst,sums)
    return -1*penalities





print(getTotalTime([2,3,9,8,4]))


# print(getTotalTime([4,2,1,3]))

print(getTotalTime([4, 2, 1, 3]) == 26)
print(getTotalTime([2, 3, 9, 8, 4]) == 88)
print(getTotalTime([4, 94, 36, 14, 47, 41]) == 1009)
print(getTotalTime([14, 32, 21, 2, 18, 49]) == 573)
print(getTotalTime([78, 57, 24, 9, 30, 78]) == 1155)
print(getTotalTime([31, 21, 2, 54, 72, 99]) == 1208)
print(getTotalTime([4, 29, 56, 49, 82, 85]) == 1268)
print(getTotalTime([48, 24, 12, 10, 72, 36]) == 850)
print(getTotalTime([18, 30, 77, 83, 60, 49]) == 1265)
print(getTotalTime([67, 44, 51, 93, 21, 12]) == 1190)
print(getTotalTime([59, 51, 65, 96, 91, 66]) == 1563)
print(getTotalTime([7, 38, 82, 22, 75, 59]) == 1186)
print(getTotalTime([7, 38, 82, 22, 75, 59]) == 1186)