def divisores(n):
    div=[]
    for i in range(1,n+1):
        if n % i ==0:
            div.append(i)

    return div


def goldbash(n):
    n_1=1
    n_2=n-1
    while len(divisores(n_1)) != 2 or len(divisores(n_2)) != 2:
        n_1+=1
        n_2-=1
    return (n_1,n_2)

assert  goldbash(4) == (2,2), "ejemplo 1 incorrecto"
assert goldbash(6) == (3,3), "ejemplo 2 incorrecto"
assert goldbash(8) == (3,5), "ejemplo 3 incorrecto"


