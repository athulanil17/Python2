c=input("Enter a string: ")
for i in c:
    frequency=c.count(i)
    print(str(i)+":"+str(frequency),end=",")
