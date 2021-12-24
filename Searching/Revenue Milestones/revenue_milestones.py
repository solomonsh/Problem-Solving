def revenue_milestones(revenues, milestones):
    reached_days = [-1]*len(milestones)

    for i in range(len(milestones)):
        revenue_sums = 0
        for j in range(len(revenues)):
            revenue_sums += revenues[j]
            if revenue_sums >= milestones[i]:
                reached_days[i] = j+1
                break
        
    return reached_days



# Test Cases

# print(revenue_milestones([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [100, 200, 500]) == [4, 6, 10])
# print(revenue_milestones([100, 200, 300, 400, 500], [300, 800, 1000, 1400]) == [2, 4, 4, 5])
# print(revenue_milestones([700, 800, 600, 400, 600, 700], [3100, 2200, 800, 2100, 1000]) == [5, 4, 2, 3, 2])
