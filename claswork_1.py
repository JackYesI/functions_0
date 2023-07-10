list_numbers = [1.5, 3.8, .9, 10, 12, 18, 7.00008, -1 ,0]

def SumFloat(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def Max(list):
    return max(list)

def checkList(list):
    count_moreZero = 0
    count_lessZero = 0
    pair = 0
    notPair = 0
    for item in list:
        if item > 0:
            count_moreZero += 1
        elif item < 0:
            count_lessZero += 1
        if item % 2:
            pair += 1
        else:
            notPair += 1
    return pair, notPair, count_moreZero, count_lessZero

def Revers(list):
    return list[-1::-1]

def Find(list, number):
    for item in list:
        if item == number:
            return True
    return False

def Factorial(list):
    list_result = []
    for item in list:
        item = int(item)
        if item > 0:
            mult = 1
            while item != 1:
                mult = mult * item
                item -= 1
            list_result.append(mult)
    return list_result
        

# print(SumFloat(list_numbers))
# print(Max(list_numbers))
# print(Factorial(list_numbers))
