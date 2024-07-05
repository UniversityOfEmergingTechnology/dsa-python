name = input("What is your name? ")

# if name == "Harry" or name == "Hermoine" or name == "Ron" :
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else :
#     print("Who ?")


# using match for pattern matching
    
match name :
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")