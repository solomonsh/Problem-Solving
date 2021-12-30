def change_in_currency(denom, target):

    denom.sort()

    if denom[0] == 1:
        return True

    p = 0
    while p< len(denom):
        coef = target//denom[p]
        if target % denom[p] == 0:
            return True
        for i in range(1, coef+1):
            temp_target = target - i*denom[p]
            if temp_target in denom:
                return True

        p += 1

    return False

# def change_in_currency_recurssion(denominations,targetMoney):
#     if targetMoney == 0:
#         return True
#     for value in denominations:
#         if value <= targetMoney:
#             if change_in_currency(denominations,targetMoney - value):
#                 return True
#     return False

# print(change_in_currency([16,17,29],75))

# print(change_in_currency([5,10,25,100,200],94)== False)


# print(change_in_currency([6,10,25,100,200],96)== True)


# print(change_in_currency([10,25,100,200],96) == False)

# print(change_in_currency([10,15,17],97) == True)
# print(change_in_currency([4, 17, 29],75) == True)
# print(change_in_currency([1, 5, 10],7) == True)
# print(change_in_currency([5, 10, 25, 100, 200],94) == False)
# print(change_in_currency([200],20) == False)
# print(change_in_currency([3, 6, 9, 12, 15],1000000) == False)
# print(change_in_currency([54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10,
#                           8, 6, 4, 2], 999999) == False)


 