import cowsay
import sys

def main():
    if len(sys.argv) == 2:
        message = "Hello , " + sys.argv[1]
        cowsay.cow(message)
    else:
        print("Please provide a name") 

if __name__ == "__main__" :
    main()