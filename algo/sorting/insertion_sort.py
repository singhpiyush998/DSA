def insertionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] > arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

def main():
    ls = [4, 2, 6, 1, 9];
    # 1st: 2 4 6 1 9
    # 2nd: 1 2 4 6 9
    # 3rd: 1 2 4 6 9
    # 4th: 1 2 4 6 9
    sortedLs = insertionSort(ls)
    print(*sortedLs)

if __name__ == "__main__":
    main();
