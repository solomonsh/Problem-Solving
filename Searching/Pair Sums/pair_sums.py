from collections import Counter

# def pair_sums(arr,k):

#     pairs = []
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j] == k:
#                 pairs.append([arr[i],arr[j]])
#     return len(pairs)


def pair_sums_optimized(arr,k):

    a_counter  = Counter(arr)
    counter = 0

    for ar in arr:
        if k-ar in a_counter and a_counter[(k-ar)]>=1:
            if k-ar == ar:
                counter += a_counter[k-ar]-1
            else:
                counter+= a_counter[k-ar]
           
            a_counter[ar] = a_counter[ar]-1
        
    return counter 


# print(pair_sums([1,2,3,4,3],6) == 2)

# print(pair_sums([1,5,3,3,3],6) == 4)
 
# print(pair_sums([1,5,3,3,3,1,5],6) == 7)
# print(pair_sums([4,4,4,4,4,4],8) == 15)

# print(pair_sums([4,4,4,3,5],8) == 4 )
# print(pair_sums([4,4],8) == 1)

# print(pair_sums([1,5,3,3,3,1,5],6))
# print(pair_sums([1,5,1,5],6))

# print(pair_sums([1,5,1],6))

# print(pair_sums([1,2,3,4],6))
 

# print(pair_sums([1, 2, 3, 4, 3], 6) == 2)
# print(pair_sums([1, 5, 3, 3, 3], 6) == 4)
# print(pair_sums([1, 1, 1, 1, 1, 1], 1) == 0)
# print(pair_sums([100, 99, 1, 51, 49, 49], 100) == 3)