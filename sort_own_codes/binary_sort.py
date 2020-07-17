def binary_search(sorted_list, number_to_find, lower=0, higher=None):
    if higher is None:
        higher = len(sorted_list)
    while lower < higher:
        mid_part = (lower + higher) // 2
        mid_value = sorted_list[mid_part]
        if mid_value < number_to_find:
            lower = mid_part + 1
        else:
            higher = mid_part
    return lower


def binary_sort(input_list):
    sorted_list = []
    for elem in input_list:
        index = binary_search(sorted_list, elem)
        sorted_list.insert(index, elem)
    return sorted_list
