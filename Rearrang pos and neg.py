arr = list(map(int, input("Enter elements: ").split()))

pos = []
neg = []

for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

i = 0
j = 0
result = []

while i < len(pos) and j < len(neg):
    result.append(neg[j])   # negative first
    result.append(pos[i])   # then positive
    j += 1
    i += 1

result.extend(neg[j:])
result.extend(pos[i:])

print("New List:", result)