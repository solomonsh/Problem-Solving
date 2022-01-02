from collections import Counter


# def compare(lst1, lst2):
#     if sum(lst1) == sum(lst2):
#         return 1
#     elif sum(lst1) > sum(lst2):
#         return lst1
#     else:
#         return lst2

# def balanced_splits(lst):
#     if len(lst) < 2:
#         return False
#     lst.sort()
#     b = [lst[-1]]
#     a = lst[:-1]
#     if compare(a, b) == 1:
#         return True
#     temp_a = a.copy()
#     temp_b = b.copy()

#     for i in range(len(a)-1, 0, -1):
#         a_counter = Counter(temp_a)
#         if compare(temp_a, temp_b) == temp_a:
#             temp_b.append(temp_a.pop(i))
#             if compare(temp_a, temp_b) == 1 and a_counter[temp_b[-1]] <= 1:
#                 return True
#             elif compare(temp_a, temp_b) == temp_a:
#                 continue
#         else:
#             return False
#     return False

def balanced_split(arr):

    total_sum = sum(arr)
    arr = sorted(arr)
    left_sum = 0
    right_sum = total_sum - left_sum

    for i in range(len(arr) - 1):
        left_sum += arr[i]
        right_sum = total_sum - left_sum

        if left_sum == right_sum and arr[i] < arr[i+1]:
            return True

        if left_sum > right_sum:
            return False

    return False




test_list1 = [2, 1, 2, 5]  # True
test_list2 = [3, 6, 3, 4, 4]  # False
test_list3 = [1, 5, 7, 1]  # True
test_list4 = [12, 7, 6, 7, 6]  # False
test_list5 = [5, 1, 6, 5, 5]  # False
test_list6 = [0]  # False
test_list7 = [0, 1, 0, 2, 3, 4]  # False
test_list8 = [0, 1, 4, 4, 2, 3]  # False
test_list9 = [1, 1, 1, 1, 1, 2, 3]  # True
test_list10 = [1, 1, 1, 1, 1, 2, 3, 4]  # True
test_list11 = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4]  # True
test_list12 = [4, 4, 4, 4, 4, 4, 8, 8, 8]  # True
test_list13 = [1,1,1,1,3,3,4]
# test_list14 = [1,1,1,1,4,4,4] 
# test_list15 = [1,1,1,1,2]

print(balanced_splits(test_list1) == True)
print(balanced_splits(test_list2) == False)
print(balanced_splits(test_list3) == True)
print(balanced_splits(test_list4) == False)
print(balanced_splits(test_list5) == False)
print(balanced_splits(test_list6) == False)
print(balanced_splits(test_list7) == False)
print(balanced_splits(test_list8) == False)
print(balanced_splits(test_list9) == True)

print(balanced_splits(test_list10) == True)

print(balanced_splits(test_list11)== True)
print(balanced_splits(test_list12) == True)

# print(balanced_splits(test_list13))

# print(balanced_splits(test_list15))


# print(balanced_splits([1, 5, 4]) == True)
# print(balanced_splits([5, 1, 6, 5, 5]) == False)
