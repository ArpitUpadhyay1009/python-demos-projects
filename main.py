# name = input("What is your name? ")
# length = len(name)
# print(length)

import random
# random_number = random.randint(0, 1)
# print(f"{'Heads' if random_number == 0 else 'Tails'}")

friends = ["Arpit", "Saumya", "Kunal", "Dharna", "Pushpendra"]
random_number = random.randint(0, len(friends) - 1)
print(friends[random_number])
