def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    first_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence

def find_last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    last_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            last_occurrence = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_occurrence

def find_occurrences(nums, target):

    first = find_first_occurrence(nums, target)
    if first == -1:
        return "Element not found in the array"
    last = find_last_occurrence(nums, target)
    return (
        f"The first occurrence of element {target} is located at index {first}\n"
        f"The last occurrence of element {target} is located at index {last}"
    )
