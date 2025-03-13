from game import Game

def get_user_menu_choice():
    """Affiche le menu et demande à l'utilisateur de choisir une option."""
    while True:
        print("\nMenu :")
        print("(g) Play a new game")
        print("(x) Show scores and exit")
        choice = input(": ").strip().lower()
        if choice in ['g', 'x']:
            return choice
        else:
            print("Invalid choice. Please choose again.")

def print_results(results):
    """Affiche les résultats du jeu."""
    print("\nGame results:")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("Thank you for playing!")

def main():
    """Fonction principale pour jouer au jeu et gérer les scores."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == 'g':
            game = Game()
            result = game.play()
            if result == "win":
                results["win"] += 1
            elif result == "loss":
                results["loss"] += 1
            else:
                results["draw"] += 1

        elif choice == 'x':
            print_results(results)
            break

if __name__ == "__main__":
    main()
