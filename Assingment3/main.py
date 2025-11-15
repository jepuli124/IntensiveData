

def menu() -> str:
    print("Please enter a number to choose from below")
    print("1: read from database")
    print("2: update database")
    print("3: exit")
    input("Enter here: ")


def read_database() -> vcid:
    print("please choose database to access (1/2/3)")


def edit_database() -> vcid:
    print("please choose database to access (1/2/3)")

def main() -> void:
    print("Welcome to database management\n")
    RUN = true
    while RUN: 
        UC = menu()
        match UC:
            case "1":
                read_database()
            case "2":
                edit_database()
            case "3":
                RUN = false
            case _:
                print("Invalid input, nothing was done")
if __name__ == "__main__":
    main()