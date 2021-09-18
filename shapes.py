import math


def area(a,b):
    return a*b


def perimeter(a,b):
    return 2*a+2*b
x = area(6,7)
print(x)

def square_root(number):
    return math.sqrt(number)


y=int(input("Enter a number"))
y = int(y)
z=square_root(y)
print(z)

def square(z):
    return z * z


def quadratic_formula(a, b, c):
    s = square(b)
    r = 4 * a * c
    x = s - r
    j = square_root(x)
    n = ((0 - b) + j) / 2 * a
    m = ((0 - b) - j) / 2 * a
    return m, n


k, l = quadratic_formula(1, 5, 6)
print(f"The result is {k} and {l}")


def hyperbole(a, b, x, y, h, k):
    i = square(a)
    m = square(b)
    l = square(x - h)
    p = square(y - k)
    v = l / i
    z = p / m
    u = (v - z)
    return u


u = hyperbole(a=3, b=3, x=5, y=4, h=0, k=0)
print(f"The result is {u} ")


def log2(x):
    return math.log(x,2)


def shannon(b,s,n):
    m=log2(1+(s/n))
    c=b*m
    return c

c=shannon(3,2,2)
print(f"The result is: {c} ")
