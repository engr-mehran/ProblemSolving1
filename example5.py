import cmath

a=6
b=8
c=2

#discriminant
d=(b**2) - (4*a*c)

s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)

print("Solution Is:",s1,s2)