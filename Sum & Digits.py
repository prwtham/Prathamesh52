no = int(input("Enter a number: "))
sum1 = 0
count = 0

while no > 0:
    temp = no % 10
    sum1 = sum1 + temp
    no = no // 10
    count = count + 1
print("Sum of the number is:", sum1)
print("Number of Digits is:", count)