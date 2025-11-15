import pymongo

def menu() -> str:
    print("Please enter a number to choose from below")
    print("1: read from database")
    print("2: update database")
    print("3: exit")
    return input("Enter here: ")


def read_database(myclient):
    UC = input("please choose database to access (1/2/3): ")
    mydb = None
    
    match UC:
        case "1":
            mydb = myclient["data3assignment1"]
        case "2":
            mydb = myclient["data3assignment2"]
        case "3":
            mydb = myclient["data3assignment3"]
        case _:
            print("missinput")
            read_database(myclient)

    print("tables: ")
    print(mydb.list_collection_names())
    UC = input("please choose database to access (name of the table): ")
    
    try:
        for x in mydb[UC].find():
            print(x)
        print("thank you for reading a database\n")
    except:
        print("error\n")
    


def edit_database(myclient):
    UC = input("please choose database to access (1/2/3): ")
    mydb = None
    
    match UC:
        case "1":
            mydb = myclient["data3assignment1"]
        case "2":
            mydb = myclient["data3assignment2"]
        case "3":
            mydb = myclient["data3assignment3"]
        case _:
            print("missinput")
            edit_database(myclient)
    print("tables: ")
    print(mydb.list_collection_names())
    UC = input("please choose database to access (name of the table): ")
    try:
        CC = mydb[UC]
        for x in CC.find():
            print(x)
        UC2 = input("would you like to add or edit data (a/e): ")
        match UC2.lower():
            case "a":
                DATA1 = input("Place a name for your entry: ")
                DATA2 = input("Place a text for your entry: ")
                CC.insert_one({"name": DATA1, "text": DATA2})
                print("Adding successful\n")
            case "e":
                DATA1 = input("Choose a name of the entry you would like to edit: ")
                DATA2 = input("Place a new text for your entry: ")
                Query = {"name": DATA1}
                edit = { "$set": {"test": DATA2} }
                print(DATA1, DATA2)
                CC.update_one(Query, edit)
                print("Update successful\n")
    except:
        print("error\n")

def main():
    print("Welcome to database management\n")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    
    RUN = True
    while RUN: 
        UC = menu()
        match UC:
            case "1":
                read_database(myclient)
            case "2":
                edit_database(myclient)
            case "3":
                RUN = False
            case _:
                print("Invalid input, nothing was done")
if __name__ == "__main__":
    main()