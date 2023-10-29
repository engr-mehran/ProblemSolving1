num = int(input("Enter the number to find its factorial :"))

factorial = 1
if num<0:
    print("Negative Number have No factorial:")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The Factorial of ",num,"is",factorial)
