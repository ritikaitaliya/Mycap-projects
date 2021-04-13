#Fibonacci sequence up to n-th term
n = int(input("How many terms? "))

# 1st two terms
a, b = 0, 1
count = 0

# check number of terms is valid or not
if n <= 0:
   flag = False
else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       flag = True
       sum = a + b
       
       #update values
       a = b
       b = sum
       count += 1
