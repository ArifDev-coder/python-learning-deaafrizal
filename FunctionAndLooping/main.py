from libs import welcome as welcome_message
from libs import helo as hello_region

region = str(input("Enter your region: "))

print(welcome_message("Arif"))

while True:
    out = hello_region(region)
    if(out != "Unknow Region"):
        print(out)
    else:
        print(out)
        break
        

# x = 1
# while x <= 100:
#     print(f"{x}%")
#     x += 1

# def plus(a, b):
#     return a + b

# print(plus(1, 2)) # 3