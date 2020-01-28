def trojkat_pascala(n, k):
    if (n == k or n == 0):
        return 1
    elif (k == 1 or k == n-1):
        return n
    return trojkat_pascala(n-1,k-1) + trojkat_pascala(n-1,k)

a = trojkat_pascala(8, 2)

print(a)



    
