print("Bienvenido al juego")

numero_ganador = int(input("Elija un numero para adivinar del 1 al 10 "))
while numero_ganador < 1 or numero_ganador > 10:
    numero_ganador = int(input("Elija un numero para adivinar del 1 al 10 "))
intentos_restantes = int(input("Cuantos intentos quiere otorgar? "))

numero_del_usuario = int(input("Adivina un numero del 1 al 10, tienes {} intentos:  ".format(intentos_restantes)))

while intentos_restantes > 1:
    if numero_del_usuario != numero_ganador and numero_del_usuario > 0 and numero_del_usuario < 11:
        intentos_restantes -= 1
        print("¡Incorrecto!")
        print("Intentos restantes: {}".format(intentos_restantes))
        numero_del_usuario = int(input("Adivina un numero del 1 al 10:  "))
    elif numero_del_usuario > 10 or numero_del_usuario < 1:
        print("¡He dicho que solo numeros del 1 al 10!")
        intentos_restantes -= 1
        print("Intentos restantes: {}".format(intentos_restantes))
        numero_del_usuario = int(input("Adivina un numero del 1 al 10:  "))
    else:
        intentos_restantes = 0
        print("¡Correcto!")
        print("¡Has ganado!")
        print("¡Hasta la próxima!")

if numero_del_usuario != numero_ganador:
    print("¡Incorrecto!")
    print("¡Has perdido!")
    print("¡Hasta la próxima!")