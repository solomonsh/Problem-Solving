def largest_triple_product(lst):

    maxs = [lst[0], lst[1], lst[2]]

    maxs.sort()

    output = [0]*len(lst)
    for i, num in enumerate(lst):

        if i < 2:
            output[i] = -1
        elif i == 2:
            output[i] = maxs[0]*maxs[1]*maxs[2]
        else:
            if num > maxs[0]:
                maxs.pop(0)
                maxs.append(num)

            output[i] = maxs[0]*maxs[1]*maxs[2]

    return output


print(largest_triple_product([1, 2, 3, 4, 5]))


print(largest_triple_product([2, 1, 2, 1, 2]))


print(largest_triple_product([2, 4, 7, 1, 5, 3]))


print(largest_triple_product([1, 2, 3, 4, 5]) == [-1, -1, 6, 24, 60])
print(largest_triple_product([2, 1, 2, 1, 2]) == [-1, -1, 4, 4, 8])
print(largest_triple_product([999, 999, 12, 2])
      == [-1, -1, 11976012, 11976012])
print(largest_triple_product([743, 286, 480, 949, 320, 488])
      == [-1, -1, 101999040, 338451360, 338451360, 344092216])
print(largest_triple_product([633, 595, 586, 465, 141, 232])
      == [-1, -1, 220708110, 220708110, 220708110, 220708110])
print(largest_triple_product([30, 39, 97, 1, 79, 52])
      == [-1, -1, 113490, 113490, 298857, 398476])
print(largest_triple_product([13, 9, 12, 20, 19, 16])
      == [-1, -1, 1404, 3120, 4940, 6080])
