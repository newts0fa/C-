import time
import random
import unittest
from merge_sort import merge_sort
from radix_sort import radix_sort
from quick_sort import quick_sort


def generate_test_data(size):
    return [random.randint(0, 100000) for _ in range(size)]


def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time


def run_benchmark():
    sizes = [100, 1000, 10000, 100000, 1000000]
    results = []

    for size in sizes:
        test_data = generate_test_data(size)

        merge_time = "-"
        if size <= 100000:
            merge_time = measure_time(merge_sort, test_data)

        radix_time = measure_time(radix_sort, test_data)
        quick_time = measure_time(quick_sort, test_data)

        results.append({
            'size': size,
            'merge_sort': merge_time,
            'radix_sort': radix_time,
            'quick_sort': quick_time
        })

    print("\nРезультаты замера времени (в секундах):")
    print(" Размер массива  Merge Sort  Radix Sort  Quick Sort ")
    for res in results:
        print(f"| {res['size']:14,} | ", end="")
        print(f"{res['merge_sort'] if isinstance(res['merge_sort'], str) else f'{res['merge_sort']:.6f}':<10} | ",
              end="")
        print(f"{res['radix_sort']:.6f} | {res['quick_sort']:.6f} |")


if __name__ == '__main__':
    print("Запуск Unit-тестов...")


    unittest.main(module='test_sorting', exit=False)

    print("\nЗапуск бенчмарка...")
    run_benchmark()
