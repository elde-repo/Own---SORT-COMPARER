def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            result.append(b.pop(0))
        else:
            result.append(a.pop(0))
    if len(a) > 0:
        result.extend(a)
    elif len(b) > 0:
        result.extend(b)
    return result


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    mid_point = len(my_list) // 2
    left_list = merge_sort(my_list[:mid_point])
    right_list = merge_sort(my_list[mid_point:])
    return merge(left_list, right_list)
