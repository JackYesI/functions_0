def showMessage():
    print("\033[30m\"Don't let the noise of others' opinions\n drown out your own inner voice.\"\n\033[33mSteve Jobs\033[0m")

def numbersCouple(a, b):
    if a > b:
        z = b
        b = a
        a = z
    elif a == b:
        return
    if a % 2 == 0:
        for i in range(a, b+1, 2):
            print(i)
    else:
        for i in range(a + 1, b+1, 2):
            print(i)

def DrawLine(sym = "-", direction = '>', number = 1):
    if direction == '>':
        print(sym*number)
    elif direction == '^':
        for i in range(0, number):
            print(sym)

def MaxFour(a, b, c , d):
    if a > b and a > c and a > d:
        return a
    if b > a and b > c and b > d:
        return b
    if c > b and c > a and c > d:
        return c
    if d > b and d > c and d > a:
        return d

def SumDiapazon(a, b):
    sum = 0
    if a > b:
        z = b
        b = a
        a = z
    for i in range(a,b+1):
        sum += i
    return sum

def easiNumber(x):
    for i in range(2, int(x / 2)):
        if x % i == 0:
            return False
    return True

def HappyNumber(x):
    one =  (x // 100000) % 10
    two = (x // 10000) % 10
    three =(x // 1000) % 10
    four = (x // 100) % 10
    five = (x // 10) % 10
    six = x % 10
    if one + two + three == four + five + six:
        return True
    return False

# showMessage()
# numbersCouple(0, 100)
# numbersCouple(1, 100)
# numbersCouple(21, 10)
# DrawLine('*', '^', 100)
# print(easiNumber(11))
# print(HappyNumber(123600))

