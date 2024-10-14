import random

def get_computer_choice(player_choice):
   
    return {
        'kamens': 'šķēres',  
        'šķēres': 'papīrs', 
        'papīrs': 'kamens'    
    }[player_choice]

def play_game():
    choices = ['kamens', 'šķēres', 'papīrs']
    
    while True:
        player_choice = input("Izvēlies (kamens, šķēres, papīrs): ").lower()
        if player_choice not in choices:
            print("Lūdzu, izvēlies derīgu gājienu!")
            continue

        computer_choice = get_computer_choice(player_choice)
        
        print(f"Tu izvēlējies: {player_choice}")
        print(f"Dators izvēlējās: {computer_choice}")
        print("Tu uzvarēji!")

        while True:  
            play_again = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").lower()
            if play_again in ['jā', 'ja', 'yes', 'да']:
                break
            elif play_again in ['ne', 'nē', 'нет', 'no']:
                print("Paldies par spēlēšanu!") 
                return
            else:
                print("Lūdzu, izvēlies 'jā' vai 'nē'!")

if __name__ == "__main__":
    play_game()


