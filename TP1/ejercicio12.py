def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

numero1 = 48
numero2 = 18
resultado = mcd(numero1, numero2)
print("El máximo común divisor (MCD) de", numero1, "y", numero2, "es:", resultado)
