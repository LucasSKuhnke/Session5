name = input("what is your name? ")
# print("Hello", name)
# age = input("How old are you "+name+"? ")
# print(name+"Based on my advanced calculations, you were born in "+str(2025-int(age)))

# lets write this in a simpler way
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name}, you were born in {2025-age2}")
except:
    print("please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
