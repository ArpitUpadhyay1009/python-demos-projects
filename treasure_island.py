print('''    ____...------------...____
               _.-"` /o/__ ____ __ __  __ /o/_`"-._
             .'     / /                    / /     '.
             |=====/o/======================/o/=====|
             |____/_/________..____..________/_/____|
             /   _/ /_     <_o#/__/#o_>     _/ /_   \
             /_________/####/_________/
              |===/!/========================/!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     /========|o|===|
              |   | |         /() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ /__     '-./uuu/.-'    __/ /__ |
              |==== .'.'^'.'.====|
          jgs |  _/o/   __  {.' __  '.} _   _/o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')
print("Welcome to treasure island")
choice1 = input("Do you want to go left or right?")
if choice1 == "right":
    print("Game over.")
else:
    choice2 = input("Do you want to wait for boat or swim?")
    if choice2 == "swim":
        print("You've been eaten by crocodiles.")
    else:
        choice3 = input("There are three doors here: Red, Blue and Yellow. Which one do you choose? ")
        if choice3 == "Red":
            print("You've burned in a fire")
        elif choice3 == "Blue":
            print("You've drowned in water")
        elif choice3 == "Yellow":
            print("You've found the golden chest!")
print("Game Over")
