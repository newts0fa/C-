def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


def counting_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output
