value=input("Enter list of characters with comma: ")
mylist=value.split(",")
lists=list(mylist)
print(lists)
str=" "
st=str.join(lists)
print("This list combined to form:",st)
print(type(st))
