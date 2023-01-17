string = input("Enter a string: ").replace("","").lower()
repeated_characters = {}

for char in string:
  
 
  if char in repeated_characters:
    
    repeated_characters[char] += 1
  else:
    
    repeated_characters[char] = 1

count=0
for x in repeated_characters:
    if repeated_characters[x]>1:
      count+=1
print("Count of repeated characters")
print(count)
