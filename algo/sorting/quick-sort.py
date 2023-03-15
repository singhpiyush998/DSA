from random import randint

def partition(arr, start, end) -> int:
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex

def randomizePartition(arr, start, end):
    pivotIndex = randint(start, end)
    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
    return partition(arr, start, end)

def quickSort(arr, start, end):
    if start >= end:
        return

    pIndex = randomizePartition(arr, start, end)
    print(pIndex)
    print(arr)
    quickSort(arr, start, pIndex - 1)
    quickSort(arr, pIndex + 1, end)

def main():
    arr = list("REVAUNIVERSITY")
    quickSort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == "__main__":
    main()
