import random
n_user = input("Enter the username: ")

name_title = str("Hello " + n_user.capitalize() + " Welcome to Zarick Games!")

print("*" *(len(name_title)+12))
print("*" * 5, name_title, "*" * 5)
print("*" *(len(name_title)+12))

retry = True

while retry:
    print(f"""
    Take a look at the glass below!

                |_|     |_|     |_|    |_|     |_|
                 1       2       3      4       5
                
    """)

    devil_says = random.randint(1, 100)
    glass = random.randint(1, 5)

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

            |_|
             {glass}
                            
    """)
    else:
        print(f"""
Sorry! You have lost the game! The ball was in glass

            |_|
             {glass}

    """)
        
    user_retry = input("Do you want to play again? (yes/no): ")
    if(user_retry.lower() == "yes" or user_retry.lower() == "y"):
        retry = True
    else:
        retry = False
        print("Thank you for playing the Zarick Games! Have a nice day!")
        print("copyright © 2025 Zarick Corporation. All rights reserved.")