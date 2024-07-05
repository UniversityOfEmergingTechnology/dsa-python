# print( int(input("Enter a number: ")) + int(input("Enter another number: ")))

# -1 0 1
# float - 1.5 or -1.5

# integer_example = 5

# float_example = 5.5


# x = float(input("Enter a number : "))
# y = float(input("Enter another number : "))

# result = x + y

# print(f"The sum of {x} and {y} is {result:,}")


# rounded_result = round(result , 4)

# print(f"Rounded result : {rounded_result}")

# 1000 - 1,000

# large_number = 1000000

# print(f"{large_number:,}")

# float_precision_example = 1.12345678901234567890
# print(float_precision_example)


# x = float(input("Enter a number : "))
# y = float(input("Enter another number : "))

# result =  x / y

# # rounded_result = round(result , 2)

# # print(f"The result of {x} divided by {y} is {rounded_result}")
# print(f"The result of {x} divided by {y} is {result:.2f}")


def square(n):
    # return n ** 3
    return pow(n , 2)

def main():
    x = int(input("Enter a number : "))
    print(f"The square of {x} is {square(x)}")

main()