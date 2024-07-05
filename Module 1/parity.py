# % modulus operator

def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print(f"{x} is Even")
    else: 
        print(f"{x} is odd")

def is_even(x):
    # if x % 2 == 0 :
    #     return True
    # else : 
    #     return False
    return x % 2 == 0
        
main()



