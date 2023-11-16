def dec(printer):
    def inner():
        printer()
        print("Welcome!")
    return inner()
@dec
def printer():
    print("Welcome!")
    print("Welcome!")

printer()
