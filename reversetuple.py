def reverse(tuples):
    new_tuples=tuples[::-1]
    return new_tuples

values=input("Enter the comma seperated values: ")
list=values.split(",")
tuples=tuple(list)

print(reverse(tuples))
