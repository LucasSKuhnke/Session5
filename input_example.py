name = input("what is your name? ")
# print("Hello", name)
# age = input("How old are you "+name+"? ")
# print(name+"Based on my advanced calculations, you were born in "+str(2025-int(age)))

# lets write this in a simpler way
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name}, you were born in {2025-age2}")
except ValueError:
    print("please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("you can not divide by 0!")
except:
    print("this is another type of error")
else: # this is for no exception
    print("Thank you for playing as expected")
finally: # this will be executed no matter what, at the very end
    print("Thanks for playing the game")
