import random

n_user = input("Enter the username: ")

name_title = str("Hello " + n_user.capitalize() + " Welcome to Zarick Games!")

print("*" *(len(name_title)+12))
print("*" * 5, name_title, "*" * 5)
print("*" *(len(name_title)+12))

retry = True

while retry:
    try:
        choose_level = int(input("Choose the level of difficulty (1=Easy/2=Medium/3=Hard): "))
    except:
        print("Invalid choice! Level automatic choosing HARDCORE MODE!")
        print("IF YOU LOSE, YOUR PC WILL BROKEN!")
        lots_of_glasses = 100 # hardcore mode
        dare_condition = True
    else:
        dare_condition = False
        lots_of_glasses = 0
        if((choose_level) == 1):
            lots_of_glasses = 5
        elif(choose_level == 2):
            lots_of_glasses = 10
        elif(choose_level == 3):
            lots_of_glasses = 20

    glass_number = " ".join([str(i).rjust(3) for i in range(1, lots_of_glasses + 1)])

    devil_says = random.randint(1, 100)
    glass = random.randint(1, lots_of_glasses)

    print(glass)

    glass_shape = "|_|"
    empty_glass = [glass_shape] * lots_of_glasses # this should still be empty
    glass_order = empty_glass.copy() # it's a new place for the ball

    glass_order[glass -1] = "|o|"
    glass_order = " ".join(glass_order)
    empty_glass = " ".join(empty_glass)

    print(f"""
    Take a look at the glass below!

                {empty_glass}
                {glass_number}
                
    """)

    print("Devil says: The ball is in glass", devil_says)

    makesure = True

    while makesure:
        choose_glass = int(input("Where is the glass containing the ball?: "))

        user_makesure = input("Are you sure you want to choose this glass? (yes/no): ")

        if(user_makesure.lower() == "yes" or user_makesure.lower() == "y"):
            makesure = False
        else:
            print("Please choose the glass again!")

    if(choose_glass == glass):
        print(f"""
Congratulations! You have won the game!

            {glass_order}
            {glass_number}
                            
    """)
    else:
        print(f"""
Sorry! You have lost the game! The ball was in glass

            {glass_order}
            {glass_number}

    """)
        if(dare_condition):
            print("Your PC is broken!")
            while True:
                random_dare_number = random.randint(1, 99)
                print(f"  L O S E R        {random_dare_number}%                 \n             :(\n {n_user}\n")
    user_retry = input("Do you want to play again? (yes/no): ")
    if(user_retry.lower() == "yes" or user_retry.lower() == "y"):
        retry = True
    else:
        retry = False
        print("Thank you for playing the Zarick Games! Have a nice day!")
        print("copyright © 2025 Zarick Co. All rights reserved.\n")