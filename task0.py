for i in range(1,101):
    if (i%3==0):
        print("frizz")
        i+=1
    elif (i%5==0):
        print("buzz")
        i+=1
    elif (i % 3 ==0) and (i % 5 == 0):
        print("frizzbuzz")
        i+=1
    else:   
        print(i)
        i +=1    
