import random

rock = '''  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissor = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

choice = int(input("Choose your option: 1 for rock, 2 for paper, 3 for scissors"))
computer_choice = random.randint(1, 3)
game = [rock, paper, scissor]
print("Your choice:")
print(game[choice-1])
print("Computer's Choice:")
print(game[computer_choice - 1])
if ((choice == 1 and computer_choice == 2) or
        (choice == 2 and computer_choice == 3) or
        (choice == 3 and computer_choice == 1)):
    print("You lose")
elif choice == computer_choice:
    print("It's a tie")
else:
    print("You win")
