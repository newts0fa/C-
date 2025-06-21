import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def parallel_quicksort(arr, num_threads=1):
    if len(arr) <= 1000 or num_threads <= 1:
        quicksort(arr, 0, len(arr) - 1)
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if num_threads > 1:
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = []
            half_threads = max(1, num_threads // 2)
            futures.append(executor.submit(parallel_quicksort, left, half_threads))
            futures.append(executor.submit(parallel_quicksort, right, half_threads))

            left = futures[0].result()
            right = futures[1].result()

    return left + middle + right


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return end - start, result


def calculate_speedup(sequential_time, parallel_time):
    return sequential_time / parallel_time if parallel_time != 0 else 0


def run_tests():
    sizes = [100, 1000, 10000, 20000, 30000, 40000, 50000]
    thread_counts = [1, 2, 4, 8]
    results = []

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        arr_copy = arr.copy()

        seq_time, _ = measure_time(parallel_quicksort, arr_copy, 1)

        parallel_times = []
        for threads in thread_counts[1:]:
            arr_copy = arr.copy()
            time_taken, _ = measure_time(parallel_quicksort, arr_copy, threads)
            parallel_times.append(time_taken)

        speedups = [calculate_speedup(seq_time, pt) for pt in parallel_times]

        results.append({
            'size': size,
            'sequential_time': seq_time,
            'parallel_times': parallel_times,
            'speedups': speedups
        })

    return results, thread_counts


def print_results(results, thread_counts):
    print("\nРезультаты тестирования многопоточной быстрой сортировки")
    print("Размер массива | Последовательная (1 поток) |", end="")

    for threads in thread_counts[1:]:
        print(f" {threads} потоков |", end="")

    print(" Speedup (2) | Speedup (4) | Speedup (8) |")
    print("-" * 120)

    for res in results:
        print(f"{res['size']:>12} | {res['sequential_time']:>25.6f} |", end="")

        for time in res['parallel_times']:
            print(f" {time:>10.6f} |", end="")

        for speedup in res['speedups']:
            print(f" {speedup:>8.2f} |", end="")

        print()


if __name__ == "__main__":
    print("Запуск тестов многопоточной быстрой сортировки...")
    results, thread_counts = run_tests()
    print_results(results, thread_counts)
