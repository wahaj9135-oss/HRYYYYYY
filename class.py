age = int(input("Please enter your age: "))
ticket= int(input("Please enter the ticket price: "))
if age < 5 :
    print("You are eligible for a free ticket.")
elif (age > 5 and age <= 12):
    disc = ticket * (50/100)
    print(f"You are eligible for a discount of ${disc:.2f}.")
elif (age >12 and age <= 59):
    print("You are not eligible for a free ticket.")
elif (age >= 60):
    disc = ticket * (30/100)
    print(f"You are eligible for a discount of ${disc:.2f}.")   



else:
    print("You are not eligible for a free ticket.")