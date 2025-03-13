# hobi = ["gaming", "reading", "coding"]

# index = 1
# urutan = 1

# print(hobi[urutan - index])

# temporary_hobby = hobi

# print(f"hobi: {hobi}")

# temporary_hobby[1] = "writing"

# print(f"temporary_hobby: {temporary_hobby}")


# glass_shape = "|_|"
# glass_order = [glass_shape] * 5 # original glass order

# empty_glass = glass_order.copy() # copy glass order
# empty_glass[1] = "|o|"

# print(glass_order)
# print(empty_glass)



# glass_shape = "|_|"
# empty_glass = [glass_shape] * 5 # this should still be empty
# glass_order = empty_glass.copy() # it's a new place for the ball

# glass_order[1 -1] = "|o|"
# glass_order = " ".join(glass_order)



# print(glass_order)

# lots_of_glasses = 5
# glass_number = " ".join([str(i).rjust(3) for i in range(1, lots_of_glasses + 1)])

# print(glass_number)









# n_user = input("Enter the username: ")

# shape = "*"*5

# name_title = str(shape + " Hello " + n_user.capitalize() + " Welcome to Zarick Games! " + shape)
# long_title = len(name_title)

# print(shape * long_title)
# print(name_title)
# print(shape * long_title)

for i in range(5):
    print("*" * ((i%3)+1))