import math

def f(x):
    return math.exp(-x) -x

def biseccion(a,b,tol):
    if f(a)*f(b)>0:
        print ("No hay raíz en el intervalo")
    else:
        while abs(b-a)>tol:
            c=(a+b)/2.0
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        return c
        
print (biseccion(10,10))

def f(x):
    return math.exp(-x) -x

def secante(x0,x1,tol):
    while abs(x1-x0)>tol:
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0=x1
        x1=x2
    return x2

print (secante(10,10))


def f(x):
    return math.exp(-x) -x

def df(x):
    return -math.exp(-x) -1

def newton (x0,tol):
    while abs(f(x0))>tol:
        x0=x0-f(x0)/df(x0)
    return x0

print (newton(10,10))

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

def biseccion(a,b,tol):
    if f(a)*f(b)>0:
        print ("No existe una raíz en este intervalo")
    else:
        while abs(b-a)>tol:
            c=(a+b)/2.0
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
        return c

def secante(x0,x1,tol):
    while abs(x1-x0)>tol:
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0=x1
        x1=x2
    return x2

def newton_raphson (x0,tol):
    while abs(f(x0))>tol:
        x0=x0-f(x0)/df(x0)
    return x0

print ("Bisección: ",biseccion(10,10))
print ("Secante: ",secante(10,10))
print ("Newton-Raphson: ",newton_raphson(10,10))