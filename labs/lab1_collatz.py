def collatz(n):
    coll=[n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            coll.append(n)

        else:
            n = 3*n +1
            coll.append(n)
    return coll
print(collatz(9))
assert collatz(9) == [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "ejemplo 1 incorrecto"
