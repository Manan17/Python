for row in range(1,7):
    if(row%2==0):
        alpha='A'
        for col in range(1,row):
            print(col,end=" ")
    else:
        for col in range(1,row):
            print(alpha,end=" ")
            alpha=chr(ord(alpha)+1)
    print("\n")

    
        
