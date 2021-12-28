import heapq


def median_stream(lst):
    output = [0]*len(lst)

    for i, v in enumerate(lst):
        if i == 0:
            temp_list = [lst[0]]
        else:
            temp_list = lst[0:i+1]
        temp_list.sort()
        if len(temp_list) == 1:
            output[i] = v
        elif len(temp_list) == 2:
            output[i] = (temp_list[0] + temp_list[1])//2
        else:
            if len(temp_list) % 2 != 0:
                output[i] = temp_list[len(temp_list)//2]
            else:
                median_index = len(temp_list)//2
                output[i] = (temp_list[median_index] +
                             temp_list[median_index-1])//2

    return output


def median_stream_optmized(arr):
    medians = []

    # storing bigger values
    min_heap = []

    # storing smaller values
    max_heap = []

    heapq.heappush(min_heap, arr[0])
    medians.append(arr[0])

    for current in range(1, len(arr)):
        if arr[current] < min_heap[0]:
            heapq.heappush(max_heap, arr[current]*-1)
        else:
            heapq.heappush(min_heap, arr[current])

        rebalance(min_heap, max_heap)

        if(len(min_heap)+len(max_heap)) % 2 == 0:
            medians.append((min_heap[0]+(max_heap[0]*-1))//2)
        else:
            medians.append(min_heap[0])
    return medians

def rebalance(min_heap, max_heap):
    if len(min_heap)-1 > len(max_heap):
        heapq.heappush(max_heap, heapq.heappop(min_heap)*-1)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, heapq.heappop(max_heap)*-1)

# print(median_stream([5, 15, 1, 3]))

# print(median_stream([2, 4, 7, 1, 5, 3]))

print(median_stream_optmized([5, 15, 1, 3]) == [5, 10, 5, 4])
# print(median_stream_optmized([2, 4, 7, 1, 5, 3]) == [2, 3, 4, 3, 4, 3])

# print(median_stream_optmized([118909791, 700266, 910518540, 704224004, 584194752]) == [118909791, 59805028, 118909791, 411566897, 584194752])
# print(median_stream_optmized([821655781, 371962661, 134165672, 509919931, 756390024]) == [821655781, 596809221, 371962661, 440941296, 509919931])
# print(median_stream_optmized([940574843, 812546008, 608939753, 147290660, 754850170]) == [940574843, 876560425, 812546008, 710742880, 754850170])
# print(median_stream_optmized([641816826, 526106912, 918864393, 865296662, 169299284]) == [641816826, 583961869, 641816826, 753556744, 641816826])
# print(median_stream_optmized([616081688, 550242654, 613849218, 93071543, 919901601]) == [616081688, 583162171, 613849218, 582045936, 613849218])
# print(median_stream_optmized([532967393, 140365306, 216368585, 871495666, 752764578]) == [532967393, 336666349, 216368585, 374667989, 532967393])
# print(median_stream_optmized([86361673, 842200102, 849027549, 788864989, 243392747]) == [86361673, 464280887, 842200102, 815532545, 788864989])
# print(median_stream_optmized([792138484, 266289965, 596895321, 73846329, 747025782]) == [792138484, 529214224, 596895321, 431592643, 596895321])
# print(median_stream_optmized([963027812, 930471055, 254401899, 868853980, 389985982]) == [963027812, 946749433, 930471055, 899662517, 868853980])
# print(median_stream_optmized([298045834, 844177996, 889606000, 109545381, 134929387]) == [298045834, 571111915, 844177996, 571111915, 298045834])
