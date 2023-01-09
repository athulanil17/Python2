def reverse(tuples):
    tup=" "
    for i in tuples:
        tup=i+tup
    return tup

values=input("Enter the comma seperated values: ")
list=values.split(",")
tuples=tuple(list)

print("Reversed tuple is:", reverse(tuples))
