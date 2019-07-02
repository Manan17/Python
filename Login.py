name=input("Enter a name = ")
x=len(name)
if(x<=3):
    print("Your name should have more than 3 letters ")
elif(x>50):
    print("Your name should have less than 50 letters")
else:
    print("You're good to go!")
