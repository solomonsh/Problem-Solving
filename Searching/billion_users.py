import math

def billion_users(lst):

    max_of_list = max(lst)

    return (math.ceil(math.log(10**9,max_of_list)))


# Test 

print(billion_users([1.5]))
print(billion_users([1.1,1.2,1.3]))

print(billion_users([1.01,1.02]))

 
