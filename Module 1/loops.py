# print("Meow")
# print("Meow")
# print("Meow")
# print("Meow")
# print("Meow")


# i = 3

# while i != 0:
#     print("Meow")
#     i -=  1
#     # i = i - 1

# i = 0

# while i < 3:
#     print("Meow")
#     i += 1

# range (start value = 0 , end value , step value = 1)
# for _ in range(1 , 11 , 2):
#     print("Meow") 

def main() :
    n = get_number()
    meow(n)

def get_number() :
    n = int(input("Enter a number : "))
    return n

def meow(n):
    for _ in range(n):
        print("Meow")


main()