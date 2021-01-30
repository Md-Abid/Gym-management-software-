# Gym Management System
# Enter your client name.This system can handle many client that you want.
client_list = {1:"Haris",  2:"Rocky",  3:"Rahim",4:"Akbar",5:"Abid"}
lock_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value,"\n", end="")
    client_name = int(input("Enter: "))
        
    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input("Enter: "))

    if op == 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value,"\n", end="")
        lock_name =  int(input("Enter: "))
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while(k != "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input("Write here: ")
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        lock_name =  int(input("Enter: "))
        print(client_list[client_name], "-", lock_list[lock_name], "Report :","\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close() 
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")