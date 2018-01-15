
pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()
while pokemon_elegido != "SQUIRTLE" and pokemon_elegido != "CHARMANDER" and pokemon_elegido != "BULBASAUR":
    pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()

vida_pikachu = 100
chance_chispazo = 9
chance_voltio = 8
vida_enemigo = 0
ataque_pokemon = 0
chance_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8
    chance_enemigo = 9

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 10
    chance_enemigo = 9

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"
    ataque_pokemon = 7
    chance_enemigo = 9

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio)").upper()
    while ataque_elegido != "CHISPAZO" and ataque_elegido != "BOLA VOLTIO":
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
            vida_enemigo -= 12
        else:
            print("¡Tu ataque ha fallado! ")

    if vida_enemigo > 0:
        print("La vida del {} enemigo ahora es de {}".format(nombre_pokemon, vida_enemigo))
    else:
        print("Has derrotado al {} enemigo".format(nombre_pokemon))

    if vida_enemigo > 0:
        ataque_enemigo = random.randint(1, 10)
        if ataque_enemigo <= chance_enemigo:
            print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
            vida_pikachu -= ataque_pokemon
        else:
            print("¡El ataque enemigo ha fallado!")
    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado")