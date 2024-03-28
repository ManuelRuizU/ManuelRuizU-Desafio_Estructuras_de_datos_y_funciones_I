
# Abrimos el archivo y leemos el texto
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

# print(texto)


# Contar caracteres distintos
caracteres_distintos = set(texto)
cantidad_caracteres_distintos = len(caracteres_distintos)

# contar palabras distintas
# .split(' ') esto me indica que en el espacio divide.
palabras = texto.split(' ')
palabras_distintas = set(palabras)
cantidad_palabras_distintas = len(palabras_distintas)



# Imprimir los resultados
print(f"El número de caracteres distintos es: {cantidad_caracteres_distintos}")
print(f"El número de palabras distintas es: {cantidad_palabras_distintas}")



