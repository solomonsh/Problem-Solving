# from itertools import permutations

# def minPermutation(lst):
#     arrangements  = list(permutations(lst,len(lst)))
#     print(arrangements)
#     total_res = []

#     for arrangement in arrangements:
#             res1  = []
#             for i in range(len(arrangement)):
#                 if i!=len(arrangement)-1:
#                     res1.append(abs(arrangement[i]-arrangement[i+1]))
#                 else:
#                     res1.append(abs(arrangement[0]-arrangement[-1]))
            
#             total_res.append(max(res1))
#             # print(total_res)
#     return min(total_res)

def minOverallAwkwardness(arr):
    arr.sort()
    arr = arr[::2] + list(reversed(arr[1::2]))
    print(arr)
    m = abs(arr[-1] - arr[0])
    for i in range(1, len(arr)):
        print(abs(arr[i]-arr[i-1]))
        m = max(m, abs(arr[i]-arr[i-1]))
    return m



print(minOverallAwkwardness([1,2,3,5,7]))  