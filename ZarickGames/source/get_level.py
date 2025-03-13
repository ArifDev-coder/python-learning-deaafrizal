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
