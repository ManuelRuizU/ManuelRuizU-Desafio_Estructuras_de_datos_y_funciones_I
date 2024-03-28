
#Desafío - Estructuras de datos y funciones (I)
import sys

# Función para convertir pesos chilenos a otras divisas
def convertir_pesos(tasas, valor_pesos):
    soles = valor_pesos * tasas[0]
    pesos_argentinos = valor_pesos * tasas[1]
    dolares = valor_pesos * tasas[2]
    return soles, pesos_argentinos, dolares

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    
    # Verifica si se proporcionan los argumentos correctos
    if len(sys.argv) != 5:
        print("Uso: python conversiones.py tasa_sol tasa_peso_arg tasa_dolar valor_en_pesos")
    else:
        # Obtiene las tasas de conversión y el valor en pesos desde los argumentos de línea de comandos
        tasas = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
        valor_pesos = float(sys.argv[4])
        
        # Realiza las conversiones y obtiene los resultados
        soles, pesos_argentinos, dolares = convertir_pesos(tasas, valor_pesos)
        
        # Muestra los resultados
        print(f"Los {valor_pesos} pesos equivalen a:")
        print(f"{soles} Soles Peruanos")
        print(f"{pesos_argentinos} Pesos Argentinos")
        print(f"{dolares} Dólares Estadounidenses")
        
        
