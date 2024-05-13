def mostrar_vector_atras_adelante(vector, indice):
    if indice < 0:
        return
    else:
        print(vector[indice])
        mostrar_vector_atras_adelante(vector, indice - 1)


mi_vector = [1, 2, 3, 4, 5]
print("Mostrando el vector desde atrás hacia adelante:")
mostrar_vector_atras_adelante(mi_vector, len(mi_vector) - 1)
