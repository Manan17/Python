
prev=0
curr=1
series = int(input("Enter series = "))
print(prev)
print(curr)
series = series-2
while(series>0):
    nextt = prev + curr
    print(nextt)
    prev=curr
    curr=nextt
    series = series-1

