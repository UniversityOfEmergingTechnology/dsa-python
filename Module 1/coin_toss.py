# import random
from random import choice , randint , shuffle


# def simulate_coin_toss() :
#     # define the two sides of a coin
#     sides = ["heads" , "tails"]

#     #randomly choose one side
#     # coin = random.choice(sides)
#     coin = choice(sides)

#     # print the result
#     print("The coin landed on " + coin)
#     # randint(a,b)
#     number = randint(1 , 100)
#     print("The number is " , number)


# simulate_coin_toss()


cards = ["Jack" , "Queen" , "King"]

shuffle(cards)

# print the shuffled cards

# print("Shuffled cards : " , cards)

for card in cards :
    print(card)