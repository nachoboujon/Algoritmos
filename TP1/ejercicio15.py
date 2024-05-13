def raiz_cuadrada_entera(numero):
    def buscar_raiz_cuadrada_entre(inicio, fin):
        if inicio == fin:
            return inicio
        mitad = (inicio + fin) // 2
        if mitad * mitad == numero:
            return mitad
        elif mitad * mitad < numero:
            return buscar_raiz_cuadrada_entre(mitad + 1, fin)
        else:
            return buscar_raiz_cuadrada_entre(inicio, mitad)
    

    return buscar_raiz_cuadrada_entre(0, numero)

numero = 16
print("Raíz cuadrada entera de", numero, "es:", raiz_cuadrada_entera(numero))
