#i = 99                                      
#while i!= 990:   
#      print(1*i)     
#      i = i+1      

i = 20
 
while (i != 1):
    if i == 5:
        break
    print(i)
    i = i - 5

a = [1,"Test",True,2,3,4,4,5,1,2,"Hello","None"]
 
x = len(a) #yesle suruma a ko len nikalo
i = 0 #index 0 bata start hunxa
while (i<x):
    f = a[i]
    if isinstance(f, int):
        if f == True:
            i = i + 1
            continue
        if a[i] == 5:
            break
        print(a[i])
    i = i + 1



    n = 100
    user_inp = int(input("enter the number"))
    if n == user_inp:
        print("you won")
    else:
        print("you lost")
