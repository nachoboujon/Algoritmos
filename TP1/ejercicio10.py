def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)


numero = 12345
print("Cantidad de dígitos:", contar_digitos(numero))
