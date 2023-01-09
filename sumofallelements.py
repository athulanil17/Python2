val=input("Enter the values: ")
l=val.split()
lists=list(l)
print(lists)
sum=0
for num in l:
    sum=sum+int(num)
    
print("the sum of all elements from the list is equal to", sum)
