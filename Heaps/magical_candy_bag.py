from heap import MaxHeap
import heapq

def magical_candy_bag(arr,k):

    sum = 0
    for i in range(k):
        current_max=max(arr)
        sum+= current_max
        arr.pop(arr.index(current_max))
        arr.append(current_max//2)
    return sum



def magical_candy_bag_with_heap(arr,k):
    max_heap = MaxHeap()
    for ar in arr:
        max_heap.add(ar)

    sum = 0
    for i in range(k):
       current_max =  max_heap.retrieve_max()
       sum+= current_max
       max_heap.add(current_max//2)

    return sum


def magical_candy_bag_with_heapq(arr,k):
    max_heap = MaxHeap()
    for ar in arr:
        max_heap.add(ar)
    
    
    sum = 0
    for i in range(k):
       current_max =  max_heap.retrieve_max()
       sum+= current_max
       max_heap.add(current_max//2)

    return sum
        
   


arr  = [2,1,7,4,2]
arr2 = [19,78,76,72,48,8,24,74,29]
# print(magical_candy_bag(arr,3))
# print(magical_candy_bag(arr2,3))


print(magical_candy_bag_with_heap(arr,3))

print(magical_candy_bag_with_heap(arr2,3))



# print(magical_candy_bag([2, 1, 7, 4, 2], 3) == 14)
# print(magical_candy_bag([19, 78, 76, 72, 48, 8, 24, 74, 28], 3) == 228)
# print(magical_candy_bag([136120699, 675464321, 262606628, 78381914, 845538549], 2093) == 3996224157)
# print(magical_candy_bag([11691841, 657719590, 998119095, 278602549, 6255378], 1816) == 3904776838)
# print(magical_candy_bag([965689668, 37220003, 58396314, 217381081, 266833901], 1364) == 3091041852)
# print(magical_candy_bag([596304821, 123652827, 498688039, 57140046, 858215077], 1123) == 4268001540)
# print(magical_candy_bag([549953320, 939734274, 901266109, 547850345, 487898284], 2327) == 6853404595)
# print(magical_candy_bag([708051013, 465222651, 537415105, 839647354, 902604158], 3703) == 6905880494)
# print(magical_candy_bag([293570508, 696546977, 513671040, 808133416, 283191606], 7706) == 5190227023)
# print(magical_candy_bag([56947285, 6178719, 895542109, 956643976, 291045423], 7965) == 4412714956)
# print(magical_candy_bag([677396178, 969219274, 63310084, 357059777, 522773324], 7778) == 5179517211)
# print(magical_candy_bag([979474204, 324566924, 545391644, 933162372, 513560358], 409) == 6592310932)





# print(magical_candy_bag_with_heap([2, 1, 7, 4, 2], 3) == 14)
# print(magical_candy_bag_with_heap([19, 78, 76, 72, 48, 8, 24, 74, 28], 3) == 228)
# print(magical_candy_bag_with_heap([136120699, 675464321, 262606628, 78381914, 845538549], 2093) == 3996224157)
# print(magical_candy_bag_with_heap([11691841, 657719590, 998119095, 278602549, 6255378], 1816) == 3904776838)
# print(magical_candy_bag_with_heap([965689668, 37220003, 58396314, 217381081, 266833901], 1364) == 3091041852)
# print(magical_candy_bag_with_heap([596304821, 123652827, 498688039, 57140046, 858215077], 1123) == 4268001540)
# print(magical_candy_bag_with_heap([549953320, 939734274, 901266109, 547850345, 487898284], 2327) == 6853404595)
# print(magical_candy_bag_with_heap([708051013, 465222651, 537415105, 839647354, 902604158], 3703) == 6905880494)
# print(magical_candy_bag_with_heap([293570508, 696546977, 513671040, 808133416, 283191606], 7706) == 5190227023)
# print(magical_candy_bag_with_heap([56947285, 6178719, 895542109, 956643976, 291045423], 7965) == 4412714956)
# print(magical_candy_bag_with_heap([677396178, 969219274, 63310084, 357059777, 522773324], 7778) == 5179517211)
# print(magical_candy_bag_with_heap([979474204, 324566924, 545391644, 933162372, 513560358], 409) == 6592310932)