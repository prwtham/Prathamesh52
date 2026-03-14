n = int(input("Enter a number: "))
temp = n
sum1 = 0

while n > 0:
    rem = n % 10
    f = 1
    for i in range(1, rem+1):
        f = f * i
    sum1 = sum1 + f
    n = n // 10

if sum1 == temp:
    print("Peterson Number")
else:
    print("Not Peterson Number")