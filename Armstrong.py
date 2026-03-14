no = int(input("Enter a number: "))
real = no
real1 = no
sum1 = 0
count = 0
while real1 > 0:
    real1 = real1 // 10
    count = count + 1

while no > 0:
    rem = no % 10
    sum1 = sum1 + rem ** count
    no = no // 10

if sum1 == real:
    print("Armstrong number")
else:
    print("Not Armstrong number")