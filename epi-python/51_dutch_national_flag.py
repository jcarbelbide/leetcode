def dutch_national_flag(arr, pivot_index):
    pivot = arr[pivot_index]
    #
    last = 0

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            arr[last], arr[i] = arr[i], arr[last]
            last += 1
    print(arr)
    last = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        if arr[i] > pivot:
            arr[last], arr[i] = arr[i], arr[last]
            last -= 1
            print(arr, i, last)
    print(arr)


if __name__ == '__main__':
    a = [3, 1, 9, -1, -4, 0, 8, 3]
    dutch_national_flag(a, 5)
