from source import play_game
from source import welcome_message as welcome
from source.loading import loading

def options():
    while True:
        print(f"Options \n1. Play Game \n2. Face Detection \n3. Exit")
        opt = int(input("Enter your choice [1/2/3/..]: "))
        if opt == 1:
            play_game.play_game()
        elif opt == 2:
            print("Face Detection is under development")
            loading()
        elif opt == 3:
            loading()
            exit()

def main():
    name = input("Enter the username: ")

    welcome.welcome_message(name)
    options()

if __name__ == "__main__":
    main()