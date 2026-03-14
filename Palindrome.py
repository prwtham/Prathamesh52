no = int(input("Enter a number: "))
rev = 0
real = no

while no > 0:
    rem = no % 10
    rev = rev * 10 + rem
    no = no // 10
if real==rev:
    print("Palindrome")
else:
    print("Not Palindrone")