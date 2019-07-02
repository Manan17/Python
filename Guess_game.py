x=9
num=0
count=0
while(count<3):
    num=int(input("Guess : "))

    if(num==9):
        print("You entered the right number !")
        break
    count=count+1

if(num!=x):
    print("Sorry better luck next time")
