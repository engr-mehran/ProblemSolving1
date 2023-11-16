def decor(addition):
    def inner():
        result=addition()
        num3=float(input("Enter third number:"))
        result=result+num3
        return result
    return inner
@decor
def addition():
    num1=float(input("Enter a first number:"))
    num2=float(input("Enter a second number:"))
    result=num1+num2
    return result

print("Addition is:",addition())