"Given an array, sort it using merge sort"

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    arr3 = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    return arr3


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr

    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)

def main():
    arr = [2,8,5,3,9,4,1,7]
    print("Original array:", arr)
    res = merge_sort(arr)
    print("Sorted array:", res)

if __name__ == "__main__":
    main()
