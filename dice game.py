import random


print("Person with the highest last number wins!!!!") 
for chance in range(1,4):
    num = random.randint(1,7)
    print(num)
    if chance<3:
        choice = input("To roll again press R = ")
    if choice == 'R' or choice == 'r':
        continue
    else:
        print("Enjoy")
        break



