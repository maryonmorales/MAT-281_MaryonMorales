def divisores(n):
    div=[]
    for i in range(1,n-1):
        if n % i ==0:
            div.append(i)

    return div

def amigos(a,b):
    div_a = divisores(a)
    div_b = divisores(b)
    sigma_a = sum(div_a)
    sigma_b = sum(div_b)
    if sigma_a == b or sigma_b == a:
        return True
    else:
        return False

assert amigos(220,284) == True, "ejemplo 1 incorrecto"
assert amigos(6,5) == False, "ejemplo 2 incorrecto"

