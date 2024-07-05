# x = int(input("What's x ?"))

# print(f"x is {x}")


# try :
#     x = int(input("What's x ?"))
# except ValueError:
#     print("You must enter an integer value for x")
# else :
#     print(f"x is {x}")


# while True :
#     try:
#         x = int(input("What's x ?"))
#         break
#     except ValueError:
#         print("You must enter an integer value for x")


# print(f"x is {x}")


# def get_int(prompt = "Enter an integer value for x ") :
#     while True :
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("You must enter an integer value for x")

# result = get_int()

# print(f"result is {result}")

# understanding pass statement

# def get_int(prompt = "Enter an integer value for x ") :
#     while True :
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass # do nothing

# result = get_int()

# print(f"result is {result}")


# user_input = input("Enter a number: ")

# if user_input.isnumeric():
#     number = int(user_input)
#     print("Number", number)
# else :
#     print("Please enter a valid number")


def main():
    x = get_int("Enter a number for X : ")
    y = get_int("Enter a number for Y : ")
    print(f"{x} and {y}") 

def get_int(prompt = "Enter an integer value") :
    try :
        return int(input(prompt))
    except ValueError:
        print("You must enter an integer value")
        # pass

main()