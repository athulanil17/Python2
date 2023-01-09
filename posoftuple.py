values=input("Enter the comma seperated values: ")
list=values.split(",")
tuples=tuple(list)
print("Tuples:", tuples)
f=input("Enter the value: ")
if f in tuples:
    indexs=tuples.index(f)
    print("Item found at position", indexs)