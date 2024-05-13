def invertir_numero(numero, invertido=0):
    if numero == 0:
        return invertido
    else:
        invertido = invertido * 10 + numero % 10
        return invertir_numero(numero // 10, invertido)

numero = 12345
print("Número invertido:", invertir_numero(numero))
