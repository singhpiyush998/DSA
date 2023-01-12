def insertionSort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i];
        j = i - 1;
        while (j >= 0 and arr[j] > tmp):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = tmp
        
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
