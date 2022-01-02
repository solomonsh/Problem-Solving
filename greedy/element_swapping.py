def findMinArray(lst, k):

    difference = 0

    for i in range(k):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                if difference <= (lst[j] - lst[j+1]):
                    difference = lst[j] - lst[j+1]
                    a = j
                    b = j+1
                if k == 1:
                    break
                if i != 0:
                    break

        lst[a], lst[b] = lst[b], lst[a]
        difference = 0
    return lst

    # for i in range(k):
    #     for j in range(len(lst)-1):

    #             if lst[j]>lst[j+1]:
    #                 if difference <= (lst[j]- lst[j+1]):
    #                     difference = lst[j]- lst[j+1]
    #                     a = j
    #                     b = j+1
    #                 if k == 1:
    #                     break
    #                 if i !=0:
    #                     break

    #     lst[a],lst[b] = lst[b],lst[a]
    #     difference = 0
    # return lst


# print(findMinArray([5,3,1],2))
# print(findMinArray([5,3,1],2))
# print(findMinArray([8,9,11,2,1],3))

# print(findMinArray([7,5,6,1],3))
# print(findMinArray([5, 6, 1, 2, 6, 7, 8, 9],3))
# print(findMinArray([8, 9, 11, 2, 1], 5))  # 1,8,9,2,11


# print(findMinArray([9,8,11,2,1],1))

 



 # print(findMinArray([8,9,11,2,1],3))

 