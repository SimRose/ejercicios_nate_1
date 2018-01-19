
pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()
while pokemon_elegido != "SQUIRTLE" and pokemon_elegido != "CHARMANDER" and pokemon_elegido != "BULBASAUR":
    pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()

vida_pikachu = 100
chance_chispazo = 9
chance_voltio = 8
vida_enemigo = 0
ataque_pokemon = 0
chance_enemigo = 0
ataque_1 = 0
ataque_2 = 0
nombre_ataque_1 = ""
nombre_ataque_2 = ""


if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_1 = 10
    ataque_2 = 9
    nombre_ataque_1 = "Burbuja"
    nombre_ataque_2 = "Coletazo"
    chance_enemigo = 9


elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    chance_enemigo = 9
    ataque_1 = 11
    ataque_2 = 10
    nombre_ataque_1 = "Llamarada"
    nombre_ataque_2 = "Garra"

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_1 = 9
    ataque_2 = 8
    nombre_ataque_1 = "Latigo"
    nombre_ataque_2 = "Ataque rapido"
    chance_enemigo = 9

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = ""
    while not (ataque_elegido == "CHISPAZO" or ataque_elegido == "BOLA VOLTIO"):
        ataque_elegido = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio)").upper()

    import random
    chance_ataque = random.randint(1, 10)
    if ataque_elegido == "CHISPAZO":
        if chance_ataque <= chance_chispazo:
            print("¡Has utilizado Chispazo!")
            vida_enemigo -= 10
        else:
            print("¡Tu ataque ha fallado! ")
    elif ataque_elegido == "BOLA VOLTIO":
        if chance_ataque <= chance_voltio:
            print("¡Has utilizado Bola voltio!")
            vida_enemigo -= 9
        else:
            print("¡Tu ataque ha fallado! ")

    if vida_enemigo > 0:
        print("La vida del {} enemigo ahora es de {}".format(nombre_pokemon, vida_enemigo))
    else:
        print("Has derrotado al {} enemigo".format(nombre_pokemon))

    if vida_enemigo > 0:
        if ataque_elegido == "BOLA VOLTIO" and chance_ataque <= chance_voltio:
            paralizar = random.randint(1, 10)
            if paralizar > 8:
                print("¡El pokemon enemigo está paralizado y no puede atacar!")
            else:
                numero_ataque = random.randint(1, 10)
                if numero_ataque > 5:
                    ataque_enemigo = ataque_1
                    nombre_ataque = nombre_ataque_1
                else:
                    ataque_enemigo = ataque_2
                    nombre_ataque = nombre_ataque_2
                chance_ataque_enemigo = random.randint(1, 10)
                if chance_ataque_enemigo <= chance_enemigo:
                    print("El {} enemigo usa {} y te hace {} de daño".format(nombre_pokemon, nombre_ataque, ataque_enemigo))
                    vida_pikachu -= ataque_enemigo
                else:
                    print("¡El ataque enemigo ha fallado!")
    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado")