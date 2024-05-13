def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + suma_digitos(numero // 10)

numero = 12345
print("Suma de los dígitos:", suma_digitos(numero))
