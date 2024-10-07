import random

def get_computer_choice():
    choices = ["kamens", "šķēres", "papīrs"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Izvēlieties (kamens, šķēres, papīrs): ").lower()
    while choice not in ["kamens", "šķēres", "papīrs"]:
        choice = input("Nepareiza izvēle. Lūdzu, izvēlieties (kamens, šķēres, papīrs): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Neizšķirts!"
    elif (user_choice == "kamens" and computer_choice == "šķēres") or \
         (user_choice == "šķēres" and computer_choice == "papīrs") or \
         (user_choice == "papīrs" and computer_choice == "kamens"):
        return "Jūs uzvarējāt!"
    else:
        return "Dators uzvarēja!"

def play_game():
    print("Laipni lūdzam spēlē 'Kamēns, šķēres, papīrs'!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Dators izvēlējās: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Vai vēlaties spēlēt vēlreiz? (jā/nē): ").lower()
        if play_again != "jā":
            break

if __name__ == "__main__":
    play_game()
