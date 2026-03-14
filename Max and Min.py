def Max(arr):
    maxx = arr[0]
    for i in arr:
        if i > maxx:
            maxx = i
    return maxx
def Min(arr):
    minn = arr[0]
    for i in arr:
        if i < minn:
            minn = i
    return minn

arr = list(map(int, input("Enter array elements: ").split()))
print("Maximum: ", Max(arr))
print("Minimum: ", Min(arr))