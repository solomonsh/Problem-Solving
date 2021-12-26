import math
def billion_users(lst):
    
    days = 1
    while True:

        total_users = 0
        for growth in lst:
            total_users += growth**days

        if total_users>=10**9:
            return days
        days+=1

 
def billion_users_optimized(lst):

    max_of_list = max(lst)

    return (math.ceil(math.log(10**9,max_of_list)))

print(billion_users([1.5]))
print(billion_users([1.1,1.2,1.3]))


print(billion_users([1.01,1.02]))

 