value = input("Enter items for the list:")
lst=list(value)
result = [[]]
for i in range(len(lst) + 1):
    for j in range(i + 1, len(lst) + 1):
        sub = lst[i:j]
        result.append(sub)

print(result)