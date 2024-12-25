import random
from posixpath import split


def ex1 (width, height):
    result = '+'
    widthEndLine = '+'
    for widthLine in range(width*2):
        result += '-'
        widthEndLine += '-'
    result += '+\n'
    widthEndLine += '+'
    for heightLine in range(height - 1):
        for widthLine in range(width*2 + 1):
            if (widthLine == 0):
                result += '|'
            elif (widthLine == width*2):
                result += ' |\n'
            else: result += ' '
    result += widthEndLine
    return result
    # Постарался чтобы при равных значениях был как можно более квадратный квадрат

def ex2 (a, b, c):
    triangle = [a, b, c]
    if triangle[0] == triangle[1] and triangle[0] == triangle[2]:
        return "Данный треугольник равносторонний"
    for triangleLine in triangle:
        sum = 0
        for triangleNumLine in triangle:
            if (triangleNumLine == triangleLine):
                continue
            sum += triangleNumLine
        if sum < triangleLine:
            return "Треугольника с такими сторонами быть не может"
    if triangle[0] == triangle[1] or triangle[0] == triangle[2] or triangle[1] == triangle[2]:
        return "Данный треугольник равнобедренный"
    return "Данный треугольник разносторонний"

def ex3 (arr = [4, 7, 20, 3, 11, 37]):
    count = 0
    for numb in arr:
        countZero = 0
        for index in range(2, numb):
            if ((numb % index) == 0):
                countZero += 1
        if (countZero == 0):
            count += 1

    return count

def ex4 (num):
    userNum = num
    usingNum = ''
    usingNumSplit = ''
    result = ''
    for index in range(num):
        result += f'{usingNum}{userNum}{"."*(userNum*2-2)}{userNum}{usingNumSplit}\n'
        usingNum += f'{userNum}'
        usingNumSplit = f'{userNum}{usingNumSplit}'
        userNum -= 1
    return result

def ex5 ():
    computerNum = 0
    more = 0
    few = 101
    userInput = input("Число 50?\nОтвет (1 - верно, 2 - больше, 3 - меньше): ")
    if (userInput == "3"):
        few = 50
    elif (userInput == "2"):
        more = 50
    elif (userInput == "1"):
        print("Угадал!")
        return
    else:
        print("Не верный ввод, экстренное завершение программы")
        return
    while(True):
        computerNum = random.randrange(more, few)
        userInput = input(f'Число {computerNum}?\nОтвет (1 - верно, 2 - больше, 3 - меньше): ')
        if (userInput == "3"):
            few = computerNum
        elif (userInput == "2"):
            more = computerNum
        elif (userInput == "1"):
            print("Угадал!")
            return

def start ():
    print("Выберете нужную программу из перечисленных:")
    print("1. Рамка\n2. Треугольник\n3. Простые числа\n4. Яма\n5. Игра")
    userAnswer = int(input("Введите число: "))
    if userAnswer == 1:
        print("Введите ширину и высоту через запятую")
        userAnswer = input("введите:").split(",")
        print(ex1(int(userAnswer[0]), int(userAnswer[1])))
    elif userAnswer == 2:
        print("Введите стороны треугольника через запятую: ")
        userAnswer = input("введите:").split(",")
        print(ex2(int(userAnswer[0]), int(userAnswer[1]), int(userAnswer[2])))
    elif userAnswer == 3:
        print("Введите числа через запятую")
        userAnswer = input("введите:").split(",")
        userAnswerInt = []
        for num in userAnswer:
            userAnswerInt.append(int(num))
        print(ex3(userAnswerInt))
    elif userAnswer == 4:
        print("Введите глубину ямы")
        userAnswer = int(input("Введите число: "))
        print(ex4(userAnswer))
    elif userAnswer == 5:
        ex5()
    else:
        print("не верный ввод")
start()