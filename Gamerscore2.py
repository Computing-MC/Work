file = open("gamerscore.csv", "r")
line = file.readline()
SearchName = str(input("Please enter a Name: "))
message=""
while(line):
    data =line.split(",")
    if data[0]== SearchName:
        print("Handle: ",data[0])
        print("Gamerscore: ",data[1])
    else:
        message="Name Not Found!"
        
    line=file.readline()
print(message)
file.close()
