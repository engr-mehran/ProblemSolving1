num = int(input("Enter the natural number for sum:"))
if num<0:
   print("please Enter a positive number")
else:
   sum=0
   while(num>0):
      sum += num
      num -=1
print("Sum is:",sum)