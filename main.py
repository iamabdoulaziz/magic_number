import random

def ask_number(min_num, max_num):
    number_int = 0
    while number_int == 0:
        number_str = input(f"Quel est le nombre magique (entre {min_num} et {max_num})? : ")
        try:
            number_int = int(number_str)
        except ValueError:
            print("ERREUR: Tu dois entrer un nombre ! Retente ta chance.")
        else:
            if number_int < min_num or number_int > max_num:
                print(f"ERREUR : Tu dois entrer un nombre entre {min_num} et {max_num}")
                number_int = 0
    return number_int


MIN_NUMBER = 1
MAX_NUMBER = 10
HEALTH = 4
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

health = HEALTH
number = 0
while not number == MAGIC_NUMBER and health > 0:
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number < MAGIC_NUMBER:
        print("Le nombre est plus grand !")
        health -= 1
        print(f"Nombre de vies: {health}")
    elif number > MAGIC_NUMBER:
        print("Le nombre est plus petit !")
        health -= 1
        print(f"Nombre de vies: {health}")
    else:
        print("Bravo, tu as trouvé le nombre magique !")

if health == 0:
    print(f"Haha t'as perdu ! Le nombre magique était : {MAGIC_NUMBER}")
""""""
