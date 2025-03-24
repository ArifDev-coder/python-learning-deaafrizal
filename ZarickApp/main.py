from source import play_game as pg
from source import welcome_message as welcome
from source.loading import loading

def options():
    while True:
        print(f"Options \n1. Play Game \n2. Face Detection \n3. Exit")
        opt = int(input("Enter your choice [1/2/3/..]: "))
        if opt == 1:
            pg.play_game()
        elif opt == 2:
<<<<<<< HEAD
            print("Face Detection is under development")
            loading()
=======
            print("Zarick Face Detection")
            load.loading()
>>>>>>> f45ce847f3b22083856d644ae13b2f2b70499e57
        elif opt == 3:
            loading()
            exit()

def main():
    name = input("Enter the username: ")

    welcome.welcome_message(name)
    options()

if __name__ == "__main__":
    main()