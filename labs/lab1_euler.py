def factorial(x):
    fac=1
    if x!=0:

        for i in range(1,x+1):
            fac = fac*i
        return fac
    else:
        return fac

def calcular_e(n):
    e=0
    for i in range(0,n):
         e += 1/factorial(i)
    return e

print(calcular_e(3))
assert calcular_e(3) == 2.5, "ejemplo 1 incorrecto"
assert calcular_e(1000) == 2.7182818284590455, "ejemplo 2 incorrecto"
