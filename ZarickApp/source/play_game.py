import socket
import random
import sys

from time import sleep
from loading import loading

pc_name = socket.gethostname()

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
        print("IF YOU LOSE, YOUR PC WILL DIE! :(")
        return 100, True

def destroying_pc():
    progress = 0
    print(f"  L O S E R   ")
    while True:
        print(f"PC Destroying... {pc_name} {progress}% :(", end='\r')
        sleep(1)
        if progress == 100:
            print("PC Destroyed...")
            sleep(5)
            print("HAHA I'm just kidding! :D\n")
            exit()
        progress +=1

def play_game():
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

                if dare_condition:
                    print("Your PC Will Destroy!")
                    destroying_pc()

                print(f"Your chance {chance}/3")
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
    print("Copyright © 2025 Zarick Co. All rights reserved.\n")
    
    loading()

if __name__ == "__main__":
    play_game()