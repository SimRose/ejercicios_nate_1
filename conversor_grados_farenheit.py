print("Bienvenido al conversor de temperatura")

farenheit = int(input("Cuantos grados Farenheit quieres convertir a Celsius? "))
celsius = int((farenheit - 32) / 1.8)

print("La temperatura en Celsius es de {} grados".format(celsius))
