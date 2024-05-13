def decimal_a_binario(numero):
    if numero <= 1:
        return str(numero)
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

numero_decimal = 23
print("Número binario correspondiente:", decimal_a_binario(numero_decimal))
