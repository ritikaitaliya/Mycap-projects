# Positive Numbers in a range
#intiation
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#iteration 
for i in range(start, end+1):
      
  #condition check
  if i > 0:
    print(i, end = " ")
