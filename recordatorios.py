
# Definir la lista de recordatorios
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
['2021-05-01', "15:00", "No trabajar"],
['2021-07-15', "13:00", "No hacer nada es feriado"],
['2021-09-18', "16:00", "Ramadas"],
['2021-12-25', "00:00", "Navidad"]]

# Agregar evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”
recordatorios.append(['2021-01-02', '06:00', 'Empezar el año'])

# Corregir evento del 15 de Julio para que sea el 16 de Julio
recordatorios[2][0] = '2021-07-16'

# Eliminar el evento del día del trabajo
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# Agregar una cena de Navidad y de Año Nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenar la lista de recordatorios por fecha
recordatorios.sort()

# Imprimir la lista de recordatorios
for evento in recordatorios:
    print('**'.join(map(str, evento)))
    
    


