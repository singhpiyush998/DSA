def sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [int(i) for i in input("Enter an array of integer: ").strip().split()]
    sort(arr)
    print("Sorted array is", *arr)

if __name__ == "__main__":
    main()
