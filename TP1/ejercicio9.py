def logaritmo_entero(n, b):
    if n < b:
        return 0
    else:
        return 1 + logaritmo_entero(n/b, b)
