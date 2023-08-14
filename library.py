
def edit(index):
    list_book.pop(index)
    list_edit = []
    for i in range(4):
        edit_ = input("Enter edit info: ")
        list_edit.append(edit_)
    for i in range(2):
        edit_ = float(input("Enter edit: "))
        list_edit.append(edit_)
    list_book.extend(index, list_edit)

def printBook():
    for i in range(len(list_book)):
        print("name: {}\nautor: {}\npublishing house: {}\ngenre: {}\nprice: {}\nrating: {}".format(list_book[i][0],list_book[i][1],list_book[i][2],list_book[i][3],list_book[i][4],list_book[i][5]))

def addBook(list_add):
    list_book.append(list_add)

def popBook(index):
    list_book.pop(index)

def search_autor(str_autor):
    for i in range(len(list_book)):
        if list_book[i][1] == str_autor:
            print("name: {}\nautor: {}\npublishing house: {}\ngenre: {}\nprice: {}\nrating: {}".format(list_book[i][0],list_book[i][1],list_book[i][2],list_book[i][3],list_book[i][4],list_book[i][5]))
            return

def search_name(str_name):
    for i in range(len(list_book)):
        if list_book[i][0] == str_name:
            print("name: {}\nautor: {}\npublishing house: {}\ngenre: {}\nprice: {}\nrating: {}".format(list_book[i][0],list_book[i][1],list_book[i][2],list_book[i][3],list_book[i][4],list_book[i][5]))
            return

def sort_alfavet_name():
    print(sorted(list_book, key=lambda list_book: list_book[0]))

def sort_alfavet_autor():
    print(sorted(list_book, key=lambda list_book: list_book[1]))

def sort_alfavet_publishing():
    print(sorted(list_book, key=lambda list_book: list_book[2]))

def sort_price():
    print(sorted(list_book, key=lambda list_book: list_book[4]))

def sort_raring():
    print(sorted(list_book, key=lambda list_book: list_book[5]))

list_book = [
    ['cat', 'erin ganter', 'acca', 'edventure', 200., 4.8],
    ['cat 1', 'erin ganter', 'acca', 'edventure', 200., 4.9],
    ['cat 2', 'erin ganter', 'acca', 'edventure', 200., 5.],
    ['cat 3', 'erin ganter', 'acca', 'edventure', 200., 4.6],
    ['cat 4', 'erin ganter', 'acca', 'edventure', 203.50, 4.6],
    ['cat 5', 'erin ganter', 'acca', 'edventure', 200., 4.7],
    ['cat 6', 'erin ganter', 'acca', 'edventure', 200., 5.0],
    ['cat 7', 'erin ganter', 'acca', 'edventure', 200., 4.5],
    ['cat 8', 'erin ganter', 'acca', 'edventure', 200., 4.4],
    ['cat 9', 'erin ganter', 'acca', 'edventure', 200., 4.0]
]

print('1) edit\n2) show book\n3) add\n4) delete\n5) search autor\n6) search name\n7) sort name\n8) sort autor\n 9) sort publish\n10) sort price\n11) sort rating\n12) menu\n13) Exit')

while True:
    choose = int(input('Enter your choose: '))
    if choose == 13:
        break
    elif choose == 12:
        print('1) edit\n2) show book\n3) add\n4) delete\n5) search autor\n6) search name\n7) sort name\n8) sort autor\n 9) sort publish\n10) sort price\n11) sort rating\n12) menu\n13) Exit')
    elif choose == 1:
        indx = int(input('Enter index: '))
        edit(indx)
    elif choose == 2:
        printBook()
    elif choose == 3:
        list_add = []
        name = input("Enter name: ")
        list_add.append(name)
        name = input("Enter autor: ")
        list_add.append(name)
        name = input("Enter publish house: ")
        list_add.append(name)
        name = input('Enter ganr): ')
        list_add.append(name)
        name = input("Enter price: ")
        list_add.append(name)
        name = input("Enter rating: ")
        list_add.append(name)
        addBook(list_add)
    elif choose == 4:
    elif choose == 5:
    elif choose == 6:
    elif choose == 7:
    elif choose == 8:
    elif choose == 9:
    elif choose == 10:



