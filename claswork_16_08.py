# open file
# read file
# write file
# close file

# url = r'C:\Users\dev\Downloads\New folder\functions_0\file\my.txt'
# file =  open(url)

# file_str = file.read() # read(5) read 5 bayt

# file_str = file.readlines()
#print(file_str, '\n Type :: ', type(file_str))

# file_str.strip() - without \n

# for line in file_str:
#     print(line.strip())

# for line in file:
#     print(line)

# file.close()

# with open(url) as file:
#     print(file.read())

# lines = [
#     '1. forse i feel it inside me',
#     '2. i am monster but i feel', 
#     '3. i feel ... better inside me',
#     'who are you jason what kind of men are you',
#     'the world on a diagonal and i am the balansic point',
#     'come on, end it',
# ]

# url = 'file/write.txt'
# # with open(url, 'a') as file:
# #     counter = 1
# #     for line in lines:
# #         file.write(f'{counter}) {line}\n')
# #         counter += 1

# with open(url, 'w') as file:
#     file.writelines(lines)

########### swap text file
# url = 'file/swap.txt'


# def readFile(fname):
#     with open(fname) as file:
#         return file.read()

# def replaceText(text, oldText, newText):
#     return text.replace(oldText, newText)

# def writeFile(fname, newText):
#     with open (fname, 'w') as file:
#         file.write(newText)

# originWord = input("Enter word > ")
# newWord = input("Enter new word > ")

# text = readFile(url)
# replace = replaceText(text, originWord, newWord)
# writeFile(url, replace)
########### swap text file

########## exersise
url = 'file/my.txt'
url_new = 'file/my_2.txt'

def readFile(fname):
    with open(fname) as file:
        return file.read()

def writeFile(fname, newText):
    with open (fname, 'w') as file:
        file.write(newText) 
    
text = readFile(url)
words = text.split()
words_reverse = list(reversed(words))
str_ = ''
for i in words_reverse:
    str_ += i + ' '
str_= str_.replace(',', '')
str_= str_.replace('.', '')


# print(len(words))