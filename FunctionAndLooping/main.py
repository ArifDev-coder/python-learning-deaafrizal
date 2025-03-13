from libs import welcome as welcome_message
from libs import helo as hello_region

def main():
    try:
        region = str(input("Enter your region: "))

        print(welcome_message("Arif"))

        while True:
            out = hello_region(region)
            if out == "Unknown Region":
                print(out)
                break
            else:
                print(out)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        
if __name__ == "__main__":
    main()

# x = 1
# while x <= 100:
#     print(f"{x}%")
#     x += 1

# def plus(a, b):
#     return a + b

# print(plus(1, 2)) # 3