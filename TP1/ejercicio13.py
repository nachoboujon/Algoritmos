def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

def mcm(a, b):
    gcd = mcd(a, b)
    return (a * b) // gcd

numero1 = 12
numero2 = 18
resultado = mcm(numero1, numero2)
print("El mínimo común múltiplo (MCM) de", numero1, "y", numero2, "es:", resultado)
