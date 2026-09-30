
ans = True
with open("Python/Part5/Sample.txt","r") as f:

    # data = f.read()
    # print(data.find("programming"))
    # for i in range[0:len(data)]:

    # data = f.readline()
    # rint(len(data))    # 5p
    # print(data)

    
    while True :
        data = f.readline()
        if "programming" in data :
            print(" Word found !")
            break
        
        print(data)        
        

