import sys
from custom_module import goodbye

# if len(sys.argv) == 2:
#     name = sys.argv[1]
#     print(f"Hello, my name is {name}")
# else :
#     print("I do not think so you have entered your name")


# try :
#     name = sys.argv[1]
#     print(f"Hello, my name is {name}")
# except IndexError :
#     print("I do not think so you have entered your name")


# if len(sys.argv) < 2 : 
#     print("Error : No name provided")
# elif len(sys.argv) > 2 :
#     print("Error : More than one name provided")
# else:
#     name = sys.argv[1]
#     print(f"Hello, my name is {name}")


# for arg in sys.argv[1:] :
#     print(arg)

# print(sys.argv[-1])



if len(sys.argv) < 2 :
    sys.exit("Error : No name provided")    
elif len(sys.argv) > 2 :
    sys.exit("Error : More than one name provided")
else :
    name = sys.argv[1]
    print(f"Hello, my name is {name}")
    goodbye(name)

