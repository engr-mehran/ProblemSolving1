def even(max):
    n=2
    yield n
    n+=2
    yield n
    n+=2
    yield n
    n+=2
    yield n

num=even(6)
print(next(num) )
print(next(num) )
print(next(num) )
print(next(num) )


def even2(max):
    n=2

    while n<=max:
        yield n
        n+=2

num1=even2(10)
print(next(num1))
print(next(num1))
print(next(num1))
print(next(num1))
        