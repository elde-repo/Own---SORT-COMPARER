def quick_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        temp = list_to_sort[-1]
        rest = list_to_sort[:-1]
        left = [item for item in rest if item < temp]
        right = [item for item in rest if item >= temp]

        return quick_sort(left) + [temp] + quick_sort(right)
