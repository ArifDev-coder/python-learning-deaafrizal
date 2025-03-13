import random

def print_title(n_user):
    shape = "="
    shape_title = shape * 5
    name_title = f"{shape_title} Hello {n_user.capitalize()} Welcome to Zarick Games! {shape_title}"
    long_title = len(name_title)

    print(shape * long_title)
    print(name_title)
    print(shape * long_title)

def get_level():
    try:
        choose_level = int(input("Choose the level of difficulty (1=Easy/2=Medium/3=Hard): "))
        if choose_level == 1:
            return 5, False
        elif choose_level == 2:
            return 10, False
        elif choose_level == 3:
            return 20, False
        else:
            raise ValueError
    except:
        print("Invalid choice! Level automatic choosing HARDCORE MODE!")
        print("IF YOU LOSE, YOUR SYSTEM WILL DIE! :(")
        return 100, True

def play_game(n_user):
    retry = True
    while retry:
        lots_of_glasses, dare_condition = get_level()
        glass_number = " ".join([str(i).rjust(3) for i in range(1, lots_of_glasses + 1)])
        devil_says = random.randint(1, 100)
        glass = random.randint(1, lots_of_glasses)

        glass_shape = "|_|"
        empty_glass = [glass_shape] * lots_of_glasses
        glass_order = empty_glass.copy()
        glass_order[glass - 1] = "|o|"
        glass_order = " ".join(glass_order)
        empty_glass = " ".join(empty_glass)

        print(f"""
        Take a look at the glass below!

                    {empty_glass}
                    {glass_number}
                    
        """)

        chance = 0
        while chance < 3:
            print("Devil says: The ball is in glass", devil_says)

            makesure = True
            while makesure:
                choose_glass = int(input("Where is the glass containing the ball?: "))
                user_makesure = input("Are you sure you want to choose this glass? (yes/no): ")

                if user_makesure.lower() in ["yes", "y"]:
                    makesure = False
                else:
                    print("Please choose the glass again!")

            if choose_glass != glass:
                chance += 1
                if chance == 3:
                    print(f"""
            Sorry! You have lost the game! The ball was in glass

                    {glass_order}
                    {glass_number}

            """)
                print(f"Your chance {chance}/3")

                if dare_condition:
                    print("Your PC is broken!")
                    while True:
                        random_dare_number = random.randint(1, 99)
                        print(f"  L O S E R        {random_dare_number}%                 \n             :(\n {n_user}\n")
            else:
                print(f"""
        Congratulations! You have won the game!

                    {glass_order}
                    {glass_number}
                                    
            """)
                break

        user_retry = input("Do you want to play again? (yes/no): ")
        retry = user_retry.lower() in ["yes", "y"]

    print("Thank you for playing the Zarick Games! Have a nice day!")
    print("copyright © 2025 Zarick Co. All rights reserved.\n")

if __name__ == "__main__":
    n_user = input("Enter the username: ")
    print_title(n_user)
    play_game(n_user)