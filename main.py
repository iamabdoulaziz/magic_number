
def ask_number(min_num, max_num):
    number_int = 0
    while number_int == 0:
        number_str = input(f"Quel est le nombre magique (entre {min_num} et {max_num})? : ")
        try:
            number_int = int(number_str)
        except ValueError:
            print("ERREUR: Tu dois entrer un nombre ! Retente ta chance.")
    return number_int


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = 5

number = 0
while not number == MAGIC_NUMBER:
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number < MAGIC_NUMBER:
        print("Le nombre est plus grand !")
    elif number > MAGIC_NUMBER:
        print("Le nombre est plus petit !")
    else:
        print("Bravo, tu as trouvé le nombre magique !")
