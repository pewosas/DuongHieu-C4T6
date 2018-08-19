n = int(input("enter the total number of 1's and 0's"))
for i in range (1, n+1):
    if i%2==0:
        print (0, " " , end='', flush=True)
    else:
        print (1, " " , end='', flush=True)