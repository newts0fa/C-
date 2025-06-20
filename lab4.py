import multiprocessing
import time
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def parallel_quick_sort(arr, num_processes):
    if num_processes <= 1:
        quick_sort(arr, 0, len(arr) - 1)
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with multiprocessing.Pool(num_processes) as pool:
        left, right = pool.map(parallel_quick_sort, [left, right])

    return left + middle + right

def generate_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

if __name__ == "__main__":
    sizes = [100, 1000, 10000, 20000, 30000, 40000, 50000]
    processes = [1, 2, 4, 8]

    print("Размер массива | 1 процесс | 2 процесса | 4 процесса | 8 процессов")
    print("-" * 60)

    for size in sizes:
        arr = generate_array(size)
        times = []

        for p in processes:
            arr_copy = arr.copy()
            time_taken = measure_time(parallel_quick_sort, arr_copy, p)
            times.append(time_taken)

        print(f"{size:12} | {times[0]:.6f} | {times[1]:.6f} | {times[2]:.6f} | {times[3]:.6f}")
