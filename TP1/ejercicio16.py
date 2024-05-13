def valor_sucesion_geometrica(a1, r, n):
    if n == 1:
        return a1
    else:
        return a1 * valor_sucesion_geometrica(a1, r, n - 1)

a1 = 2
r = -3
n = 5

an = valor_sucesion_geometrica(a1, r, n)
print("El valor de a{} en la sucesión es: {}".format(n, an))
