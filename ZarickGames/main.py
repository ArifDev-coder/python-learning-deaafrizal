from source import play_game
from source import welcome_message as welcome

def main(name):
    welcome.welcome_message(name)

if __name__ == "__main__":
    name = input("Enter the username: ")

    main(name)
    play_game.play_game()