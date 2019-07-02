command=" " 
started = False
while command!="quit":
    command=input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Ready Steady Po!......")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
    elif command == "quit":
        break
    elif command == "help":
        print('''Type:
start - to start the car
stop - to stop the car
quit - to exit''')
    else:
        print("Sorry I don't understand this ")
