n=int(input("Enter n: "))
x=int(input("Enter x: "))
sum=1 
for i in range(1,n):
    sum=sum+(x**i)/i 
print(sum)