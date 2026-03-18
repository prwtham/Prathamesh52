def arrnextlargerelement(arr, N):
    n = len(arr)
    result = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break

    return result


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    
    result1 = arrnextlargerelement(arr, N)
    print(result1)