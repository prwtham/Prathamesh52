n1 = int(input("Enter a Number 1: "))
n2 = int(input("Enter a Number 2: "))
n3 = int(input("Enter a Number 3: "))

if (n1 >= n2 and n1 >= n3):
    print("Largest Number is ", n1)

elif (n2 >= n1 and n2 >= n3):
    print("Largest Number is ", n2)

else:
    print("Largest Number is ", n3)