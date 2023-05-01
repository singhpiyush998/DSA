from itertools import accumulate


def countingSort(ls):
    freq = [0] * (max(ls) + 1)

    for i in ls:
        freq[i] += 1

    prefixSum = list(accumulate(freq))
    res = [0] * len(ls)

    for j in range(len(ls) - 1, -1, -1):
        res[prefixSum[ls[j]] - 1] = ls[j]
        prefixSum[ls[j]] -= 1

    return res


def main():
    ls = [2, 9, 7, 4, 1, 8, 4]
    res = countingSort(ls)
    print("Sorted array is:", *res)


if __name__ == "__main__":
    main()