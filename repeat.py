string = input("Enter a string: ")

repeated_characters = {}

for char in string:
  
 
  if char in repeated_characters:
    
    repeated_characters[char] += 1
  else:
    
    repeated_characters[char] = 1


print(repeated_characters)