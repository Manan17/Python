try:
    a=int(input("Enter a number = "))
    b=int(input("Enter a number = "))
    c=a/b
    print("a/b = %d"%c)

except Exception:
    print("Can't divide by zero")
else:
    print("Right")
