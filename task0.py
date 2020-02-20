for i in range(1,101):
    if (i%3==0):
        print("frizz")
        i+=1
    if (i%5==0):
        print("buzz")
        i+=1
    if (i % 3 ==0) or (i % 5 == 0) and (i % 15 != 0):
        print("frizzbuzz")
        i+=1
    
    print(i)
    i +=1
