# initialization
text = str(input("Please enter a string: "))
dict = {}

#condition check
for char in text:
  if char in dict:
    dict[char] += 1
  else:
    dict[char] = 1
    
# execution 
print ("Count of the most frequent character is:")
print (sorted(dict.items(), key = lambda x:x[1], reverse = True))
