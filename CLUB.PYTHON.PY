import json


cuota_mensual_base = 1200

adicional_gym = 3000  # Montos adicionales para cada deporte.

adicional_yoga = 3200

adicional_futbol = 3600

adicional_natacion = 3800

cuota_gym_benefx2 = adicional_gym * 60 / 100

cuota_yoga_benefx2 = adicional_yoga * 60 / 100

cuota_futbol_benefx2 = adicional_futbol * 60 / 100

cuota_natacion_benefx2 = adicional_natacion * 60 / 100


"""Diccionario con información de los deportes y sus costos.
Las claves del diccionario: (1, 2, 3, 4) que el usuario puede elegir para seleccionar un deporte.
Para cada clave, se almacena otro diccionario que contiene el nombre del deporte y los costos para las frecuencias "1" y "2" veces por semana"""

deportes = {
    "1": {
        "nombre": "Gym",
        "1": cuota_mensual_base + adicional_gym,
        "2": cuota_mensual_base + adicional_gym + cuota_gym_benefx2,
    },
    "2": {
        "nombre": "Yoga",
        "1": cuota_mensual_base + adicional_yoga,
        "2": cuota_mensual_base + adicional_yoga + cuota_yoga_benefx2,
    },
    "3": {
        "nombre": "Futbol",
        "1": cuota_mensual_base + adicional_futbol,
        "2": cuota_mensual_base + adicional_futbol + cuota_futbol_benefx2,
    },
    "4": {
        "nombre": "Natacion",
        "1": cuota_mensual_base + adicional_natacion,
        "2": cuota_mensual_base + adicional_natacion + cuota_natacion_benefx2,
    },
}


horarios = {
    "Gym": ["Lunes 9:00 AM", "Miércoles 6:00 PM", "Viernes 8:30 AM"],
    "Yoga": ["Martes 7:30 AM", "Jueves 6:00 PM"],
    "Futbol": ["Lunes 5:00 PM", "Miércoles 7:00 PM", "Viernes 4:30 PM"],
    "Natacion": ["Martes 5:30 PM", "Jueves 4:00 PM", "Sábado 10:00 AM"],
}


print("¡Bienvenidos/as a Club Py")

print()


# Guardar datos MODO ESCRITURA

with open("deportes.json", "w") as file:
    json.dump(deportes, file, indent=4)


with open("horarios.json", "w") as file:
    json.dump(horarios, file, indent=4)


# Cargamos datos desde archivos JSON MODO LECTURA

with open("deportes.json", "r") as file:
    deportes = json.load(file)


with open("horarios.json", "r") as file:
    horarios = json.load(file)


print("Los deportes que encontrarán en Club Py son:")

print()

for clave, valor in deportes.items():
    nombre_deporte = valor["nombre"]

    costo_una_vez = valor["1"]

    costo_dos_veces = valor["2"]

    print(f"{nombre_deporte}, una vez por semana: ${costo_una_vez}")  # fstrings

    print(f"{nombre_deporte}, dos veces por semana: ${costo_dos_veces}")

    print()


print("Los Horarios que encontrarán en Club Py Son:")

print()

for deporte, horario in horarios.items():
    print(deporte + ":")

    for h in horario:
        print(h)

    print()


deporte_elegido = ["GYM", "YOGA", "FUTBOL", "NATACION"]

frecuencia_semanal = ["1", "2"]

acompañante = ["si", "no"]


while True:
    opcion = input(
        """Elige uno de los deportes que quieres practicar: 

                    1- Gym

                    2- Yoga

                    3- Futbol

                    4- Natacion\n"""
    )

    frecuencia_semanal = input(
        """Elige cantidad de veces por semana:

                    1- Una vez por semana

                    2- Dos veces por semana\n"""
    )

    if opcion in ["1", "2", "3", "4"] and frecuencia_semanal in ["1", "2"]:
        deporte = deportes[opcion][frecuencia_semanal]  # costo del deporte

        nombre_deporte = deportes[opcion]["nombre"]

        if (
            frecuencia_semanal == "1"
        ):  # Hice esto para que no me quedara 1 vez por semana o 2 vez por semana
            mensaje_frecuencia = "vez por semana."

        else:
            mensaje_frecuencia = "veces por semana."

        print(
            "Elegiste practicar el deporte",
            nombre_deporte,
            frecuencia_semanal,
            mensaje_frecuencia,
        )

        print("El costo total es: $", int(deporte))

        cuota_total = deporte  # asignar el costo del deporte seleccionado a la variable cuota_total

        break

    else:
        print("Opción inválida. Por favor, elige una opción válida.")


acompañante = input(
    "\n¿Quieres aprovechar un descuento del 20% y llevar un acompañante? (si/no)\n"
)


if acompañante == "si":
    descuento_acompañante = cuota_total * 20 / 100

    cuota_total -= descuento_acompañante

    print("El costo total con descuento de acompañante es: $",int(cuota_total),".","Muchas gracias!",)

elif acompañante == "no":
    print("El costo total es: $", int(cuota_total), ".", "Muchas gracias!")

else:
    while True:
        print("Opción inválida. Por favor, elige 'si' o 'no'")
        acompañante = input("¿Quieres aprovechar un descuento del 20% y llevar un acompañante? (si/no)\n")
        if acompañante == "si" or acompañante == "no":
            if acompañante == "si":
                descuento_acompañante = cuota_total * 20 / 100
                cuota_total -= descuento_acompañante
                print("El costo total con descuento de acompañante es: $",int(cuota_total),".","Muchas gracias!",)
            else:
                print("El costo total es: $", int(cuota_total), ".", "Muchas gracias!")
            break
