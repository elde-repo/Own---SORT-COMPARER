def heappush(data_list, item):
    data_list.append(item)
    item_index = len(data_list) - 1
    while True:
        parent_index = (item_index - 1) // 2
        if data_list[item_index] > data_list[parent_index]:
            data_list[parent_index], data_list[item_index] = data_list[item_index], data_list[parent_index]
            if parent_index == 0:
                break
            item_index = parent_index
        else:
            break


def heappop(data_list):
    buf = data_list.pop()
    if len(data_list) == 0:
        return buf
    result = data_list[0]
    data_list[0] = buf
    current_index = 0
    while True:
        left_child = 2 * current_index + 1
        right_child = 2 * current_index + 2
        biggest_child = 0
        if left_child >= len(data_list):
            break
        elif right_child >= len(data_list):
            biggest_child = left_child
        elif data_list[left_child] >= data_list[right_child]:
            biggest_child = left_child
        else:
            biggest_child = right_child
        if data_list[biggest_child] > data_list[current_index]:
            data_list[biggest_child], data_list[current_index] = data_list[current_index], data_list[biggest_child]
            current_index = biggest_child
        else:
            break
    return result


def heap_sort(my_list):
    heap_data = []
    for i in range(len(my_list)):
        heappush(heap_data, my_list[i])
    sorted_list = []
    for i in range(len(my_list)):
        sorted_list.append(heappop(heap_data))
    return sorted_list
