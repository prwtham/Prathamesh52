def Rem(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                arr[j] = None
    for i in arr:
        if i != None:
            print(i, end=" ")

arr = list(map(int, input("Enter the Element: ").split()))
print("New List:", end=" ")
Rem(arr)