def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[minIndex]):
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]


def main():
    arr = [6, 8, 3, 5, 9, 10, 7, 2, 4, 1]
    selectionSort(arr)
    print(*arr)

if __name__ == "__main__":
    main()
