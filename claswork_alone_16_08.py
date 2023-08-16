# url = 'file/First_exersise.txt'
# url_2 = 'file/First_exersise_new.txt'


# def readFile(fname):
#     with open(fname) as file:
#         return file.read()

# def seven_letters(oldText):
#     list_ = oldText.split(' ')
#     newText = ''
#     for i in list_:
#         if len(i) >= 7:
#             newText += i + ' '
#     return newText

# def writeFile(fname, newText):
#     with open (fname, 'w') as file:
#         file.write(newText)

# text = readFile(url)
# newText = seven_letters(text)
# writeFile(url_2, newText)

###### Second
# url = 'file/Second_exersise.txt'
# url_2 = 'file/Second_exersise_new.txt'


# def readFile(fname):
#     with open(fname) as file:
#         return file.readlines()
    
# text = readFile(url)

# print(text)

# with open(url_2, 'w') as file:
#     newNumber = []
#     for i in text:
#         newNumber.append(i)
#     file.write("".join(newNumber))

###### Third
url = 'file/Third_exersise.txt'
url_2 = 'file/Third_exersise_new.txt'

def readFile(fname):
    with open(fname) as file:
        return file.readlines()
    
with open(url_2, 'w') as file:
    newNumber = []
    for i in text:
        newNumber.append(i)
    file.write("".join(newNumber))
    
