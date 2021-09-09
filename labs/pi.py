def calcular_pi(n):
    pi=0
    pidiv4=0
    for i in range(1,n+1):
        pidiv4 = pidiv4 + ((-1)**(i+1))/(2*i-1)

    pi=4*pidiv4
    return pi

print(calcular_pi(3))
assert calcular_pi(3) == 3.466666666666667, 'ejemplo 1 incorrecto'
assert calcular_pi(1000) == 3.140592653839794, 'ejemplo 2 incorrecto'