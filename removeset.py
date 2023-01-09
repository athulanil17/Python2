val = input("Enter the values to be entered:")
set_val=set(val)
print("Original Set: ",set_val)
inp = input("Enter the element to be removed: ")
if inp in set_val:
    set_val.remove(inp)
    print("Updated Set: ",set_val)
else:
    print("Element not present in the Set")