import random

from sort_own_codes.quick_sort import quick_sort
from sort_own_codes.binary_sort import binary_sort
from sort_own_codes.merge_sort import merge_sort
from sort_own_codes.heap_sort import heap_sort


def timer(times):
    def function_wrapper(decorated_function):
        from functools import wraps
        from datetime import datetime

        @wraps(decorated_function)
        def wrapper(*args, **kwargs):
            timing_list = []
            for item in range(times):
                t1 = datetime.now()
                result = decorated_function(*args, **kwargs)
                t2 = datetime.now() - t1
                timing_list.append(t2.total_seconds())
            mean_timing = sum(timing_list) / len(timing_list)
            print(f"{decorated_function.__name__.upper().replace('_', ' ')} - "
                  f"mean execution time: {round(mean_timing, 4)}")
            return result

        return wrapper

    return function_wrapper


if __name__ == '__main__':

    quick_sort = timer(times=10)(quick_sort)
    binary_sort = timer(times=10)(binary_sort)
    merge_sort = timer(times=10)(merge_sort)
    heap_sort = timer(times=10)(heap_sort)
    python_sort = timer(times=10)(sorted)

    list_to_sort = []
    for _ in range(10000):
        list_to_sort.append(random.randint(0, 100000))

    quick_sort(list_to_sort)
    binary_sort(list_to_sort)
    merge_sort(list_to_sort)
    heap_sort(list_to_sort)
    python_sort(list_to_sort)
