c = 0
E = 0
x = 0
x1 = c
x2 = c

changex = 10**-8


def function(n):
    return n**2


def derive(n):
    return (function(n + changex) - function(n - changex))/2*changex


def linear(n):
    return function(c) + (derive(c)*(x-c))


for i in range (0,1001):
    if (abs(function(x1)-linear(x1))==E) and x1<c:
        print()
    else:
        x1 = x1 - 0.0001

    if (abs(function(x2)-linear(x2))==E) and x2>c:
        print()
    else:
        x2 = x2 + 0.0001

if (abs(function(x1)-linear(x1))!=E) and (abs(function(x2)-linear(x2))!=E):
    print("x1 and x2 values cannot be found")
else:
    print("x1 is " + x1 + ", x2 is " + x2)
