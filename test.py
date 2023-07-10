# def showMessage(name = 'Word'):
#     print("Hello {}".format(name))
# ########################
# # питання на рахунок 
# showMessage()

# a = 10
# b = 1

# def div(a,b=1):
#     res = a / b
#     return res
# ######################
# # div()
# print(div(20))
# print(div(32))
# print(div(9))

#######################

# def sum(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     if b == 0:
#         return
#     return a / b

# def calculate(a,b,op):
#     match op:
#         case '+':
#             return sum(a,b)
#         case '-':
#             return sub(a,b)
#         case '*':
#             return mult(a,b)
#         case '/':
#             return div(a,b)

# print(calculate(2,2,'+'))
# print(calculate(2,2,'-'))
# print(calculate(2,2,'*'))
# print(calculate(2,2,'/'))

# def getOperatin(line):
#     if line.find('+') != -1:
#         return '+'
#     if line.find('-') != -1:
#         return '-'
#     if line.find('*') != -1:
#         return '*'
#     if line.find('/') != -1:
#         return '/'

# reg = input("Enter ex (2+2) > ")
# op = getOperatin(reg)
# numbers = reg.split(getOperatin(op))
# numbers = [float(numb) for numb in numbers]
# print('Result ::', calculate(numbers[0], numbers[1], op))
#######################################


