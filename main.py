import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        merged.extend(left[left_index:])
    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged

if __name__ == "__main__":
    random_list = [random.randint(1, 100) for _ in range(20)]
    print("Original list:", random_list)

    sorted_list = merge_sort(random_list)
    print("Sorted list:", sorted_list)
