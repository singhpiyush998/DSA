from random import randint

# def partition(arr, start, end) -> int:
#     pivot = arr[end]
#     pIndex = start
#     for i in range(start, end):
#         if arr[i] <= pivot:
#             arr[i], arr[pIndex] = arr[pIndex], arr[i]
#             pIndex += 1
#     arr[pIndex], arr[end] = arr[end], arr[pIndex]
#     return pIndex

# def partition(arr, left, right):
#     pivot = arr[left]
#     print("Pivot: ", pivot)
#     j = right
#     i = left + 1
#     while i <= j:
#         if arr[i] > pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             j -= 1
#         else:
#             i += 1
#
#     arr[j], arr[left] = arr[left], arr[j]
#     return j

# def partition(arr, start, end):
#     piv = arr[start]
#     i = start + 1
#     for j in range(i, end + 1):
#         if arr[j] < piv:
#             arr[j], arr[i] = arr[i], arr[j]
#             i += 1
#
#     arr[start], arr[i - 1] = arr[i - 1], arr[start]
#     return i - 1
#
# def randomizePartition(arr, start, end):
#     pivotIndex = randint(start, end)
#     arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
#     return partition(arr, start, end)
#
# def quickSort(arr, start, end):
#     if start >= end:
#         return
#
#     pIndex = randomizePartition(arr, start, end)
#     quickSort(arr, start, pIndex - 1)
#     quickSort(arr, pIndex + 1, end)

def partition(arr, low, high):
    swap_index = low
    pivot = arr[high]

    for curr_index in range(low, high):
        if arr[curr_index] <= pivot:
            arr[swap_index], arr[curr_index] =  arr[curr_index], arr[swap_index]
            swap_index += 1

    arr[swap_index], arr[high] = arr[high] ,arr[swap_index]

    return swap_index


def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)

def main():
    arr = [55, 32, 45, 67, 44, 23, 16, 89]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == "__main__":
    main()
