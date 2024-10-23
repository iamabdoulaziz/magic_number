
MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = 5

def ask_number(min_num, max_num):
    user_number = int(input(f"Quel est le nombre magique (entre {min_num} et {max_num})? : "))
    return user_number


number = ask_number(MIN_NUMBER, MAX_NUMBER)
def verify_number():
    if number < 5:
        print("Le nombre est plus grand !")
    elif number > 5:
        print("Le nombre est plus petit !")
    else:
        print("Bravo, tu as trouvé le nombre magique !")


while number != 5:
    verify_number()
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    while number == 5:
        print("Bravo, tu as trouver le nombre magique !")
        break
