# name = input("What is your name? ")
# length = len(name)
# print(length)

# import random
# random_number = random.randint(0, 1)
# print(f"{'Heads' if random_number == 0 else 'Tails'}")

# friends = ["Arpit", "Saumya", "Kunal", "Dharna", "Pushpendra"]
# random_number = random.randint(0, len(friends) - 1)
# print(friends[random_number])

scores = [100, 99, 45, 120, 453, 65, 66, 7, 233, 2, 5343, 6, 2, 2, 43434, 3, 4, 43, 4, 3, 35, 53545354, 653, 5346, 4, 3]
max_score = -1
for score in scores:
    if score > max_score:
        max_score = score
print(f"The maximum score is {max_score}")
