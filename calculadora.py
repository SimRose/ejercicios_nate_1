operacion_elegida = input("Que operación deseas ejecutar? (multiplicar / dividir / sumar / restar): ").upper()
while operacion_elegida != "MULTIPLICAR" and operacion_elegida != "DIVIDIR" and operacion_elegida != "SUMAR" and operacion_elegida != "RESTAR":
    print ("Elija una opción valida")
    operacion_elegida = input("Que operación deseas ejecutar? (multiplicar / dividir / sumar / restar): ").upper()

primer_numero = int(input("¿Cual es el primer numero?: "))
segundo_numero = int(input("¿Cual es el segundo numero?: "))

if operacion_elegida == "MULTIPLICAR":
    multiplicacion = primer_numero * segundo_numero
    print("El resultado es {}".format(multiplicacion))
elif operacion_elegida == "DIVIDIR":
    dividision = primer_numero / segundo_numero
    print("El resultado es {}".format(dividision))
elif operacion_elegida == "SUMAR":
    suma = primer_numero + segundo_numero
    print("El resultado es {}".format(suma))
elif operacion_elegida == "RESTAR":
    resta = primer_numero - segundo_numero
    print("El resultado es {}".format(resta))

print("Gracias por utilizar esta calculadora, hasta luego")



