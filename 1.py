import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def analyze_time_complexity(sort_function):
    input_sizes = [1000, 10000, 100000, 1000000]
    for size in input_sizes:
        input_list = [random.randint(0, size) for _ in range(size)]
        start_time = time.time()
        sort_function(input_list)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Input size: {size}, Execution time: {execution_time}")

# Example usage
analyze_time_complexity(quicksort)
