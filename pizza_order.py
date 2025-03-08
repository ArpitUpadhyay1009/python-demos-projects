print("Welcome to pizza order")
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on you pizza? Y for yes and N for no: ")
cheese = input("Do you want extra cheese on your pizza? Y for yes and N for no: ")
bill = 0
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
if cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}.")
