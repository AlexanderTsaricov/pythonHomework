# Task 1
from random import Random


class Parent:
    def __init__(self, name, age):
        print('parent is create')
        self.kids = []
        self.name = name
        self.age = age
    def getInfo(self):
        print(f'i am are {self.name} and i {self.age} years old. Child -{self.getChilds()}' )
    def getChilds(self):
        result = ''
        if len(self.kids) > 0:
            for i in self.kids:
                result += f' {i.name}, '
        else:
            'do not have'
        return result
    def calmChild(self, child):
        child.hunger = True
        print(f'{child.name} is calm')
    def feedTheBaby(self, child):
        child.mood = True
        print(f'{child.name} is feed')
    def initChild(self, name, age, hunger, mood):
        if ((self.age - age) >= 16):
            kid = Child(name, age, hunger, mood)
        else:
            kid = Child(name, 0, hunger, mood)
        self.kids.append(kid)
        return kid

class Child(Parent):
    def __init__(self, name, age, hunger = True, mood = True):
        print('child is create')
        self.hunger = hunger
        self.mood = mood
        super().__init__(name, age)

# Task 2


class People:
    __max_hungry = 100
    def __init__(self, name, home):
        self.name = name
        self.hungry = 50
        self.home = home
        self.alive = True
        self.howMuchPay = 0
        self.howMuchGame = 0
        self.howMuchWork = 0
        self.howMuchEat = 0
    def eatFood(self):
        self.hungry += 10
        self.home.food -= 10
        print(f'{self.name} поел, голод: {self.hungry}, еды дома: {self.home.food}')
        self.howMuchEat += 1
    def work(self):
        self.hungry -= 10
        self.home.money += 10
        print(f'{self.name} поработал, голод: {self.hungry}, денег дома: {self.home.money}')
        self.howMuchWork += 1
    def game(self):
        self.hungry -= 5
        print(f'{self.name} поиграл, голод: {self.hungry}')
        self.howMuchGame += 1
    def payFood(self):
        print(f'{self.name} покупает еду')
        self.home.food += 20
        self.home.money -= 20
        print(f'Еды дома: {self.home.food}, Денег дома: {self.home.money}')
        self.howMuchPay += 1
    def liveOneDay(self):
        rand = Random()
        rnd = rand.randint(1, 6)
        if self.hungry < 20:
            self.eatFood()
        elif self.home.food < 10:
            self.payFood()
        elif self.home.money < 50:
            self.work()
        elif rnd == 1:
            self.work()
        elif rnd == 2:
            self.eatFood()
        else:
            self.game()
        if self.hungry < 0:
            self.alive = False
            print(f'{self.name} умер')


class Home:
    def __init__(self):
        self.food = 50
        self.money = 0


def playTask2():
    home = Home()
    p1 = People('Саша', home)
    p2 = People('Света', home)

    for i in range(365):
        if p1.alive:
            p1.liveOneDay()
        if p2.alive:
            p2.liveOneDay()
    print(f'Саша: {p1.howMuchWork = }, {p1.howMuchGame = }, {p1.howMuchEat = }, {p1.howMuchPay = }')
    print(f'Света: {p2.howMuchWork = }, {p2.howMuchGame = }, {p2.howMuchEat = }, {p2.howMuchPay = }')

#  Task 3

class Cell:
    def __init__(self):
        self.valueCell = "N"


class Board:
    def __init__(self):
        self.board = [
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()]]

    def changeCell(self, value):
        if self.board[value[0]][value[1]] == "N":
            self.board[value[0]][value[1]] = value[2]
            return True
        else:
            return False

    """
    location = 0 horizontal
    location = 1 vertical
    location = 2 diagonal
    """
    def __createLine(self, location, numLine):
        line = []
        if location == 0:
            for i in range(3):
                line.append(self.board[numLine][i])
        if location == 1:
            for i in range(3):
                line.append(self.board[i][numLine])
        if location == 2:
            if numLine == 0:
                line = [self.board[0][0], self.board[1][1], self.board[2][2]]
            else:
                line = [self.board[0][2], self.board[1][1], self.board[2][0]]
        return line

    def win(self):
        for location in range(3):
            for cell in range(3):
                line = self.__createLine(location, cell)
                if line[0] != "N" and line[1] != "N" and line[2] != "N":
                    if line[0] == line[1] and line[1] == line[2]:
                        return True
        return False


class Player:
    def __init__(self, nickName, board, label):
        self.nickName = nickName
        self.wins = 0
        self.board = board
        self.label = label
    def move(self):
        playerInput = input(f'{self.nickName} введите номер клетки через запятую,\nгде 1 цифра - ориентация, 2 - номер клетки: ')
        playerInputList = playerInput.split(',')
        playerInputList[0] = int(playerInputList[0])
        playerInputList[1] = int(playerInputList[1])
        playerInputList.append(self.label)
        print(playerInputList)
        if self.board.changeCell(playerInputList):
            print(f'{self.nickName} ходит')
            return True
        else:
            print(f'Не верный ход, ячейка занята')
            return False


class Game:
    def __init__(self, player1, player2, board):
        self.state = True
        self.players = [player1, player2]
        self.board = board
        self.lastMove = 0

    def __printBoard(self):
        for line in self.board.board:
            print(f'{line[0]} {line[1]} {line[2]}')

    def move(self, player):
        if player.move():
            return True
        else:
            return False
    def playGame(self):
        self.__printBoard()
        for i in range(3):
            for j in range(3):
                self.board.board[i][j] = "N"
        flag = True
        countPlayer = self.players[0]
        while flag:
            resultMove = self.move(countPlayer)
            self.__printBoard()
            if self.board.win():
                self.__printBoard()
                print(f'{countPlayer.nickName} win!')
                countPlayer.wins += 1
                print(f'Победы {self.players[0].nickName}: {self.players[0].wins}, ')
                print(f'Победы {self.players[1].nickName}: {self.players[1].wins}, ')
                return True
            if resultMove:
                if countPlayer == self.players[0]:
                    print(f'Теперь ходит {self.players[1].nickName}')
                    countPlayer = self.players[1]
                else:
                    print(f'Теперь ходит {self.players[0].nickName}')
                    countPlayer = self.players[0]
            if 'N' not in [cell for row in self.board.board for cell in row]:
                print("Ничья")
                return True
        return False

    def start(self):
        ask = 1
        while ask:
            self.playGame()
            ask = int(input('Давайте играть?\n1 - да, 0 - нет: '))


# Task 4

class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth
    def depth(self):
        if self.max_depth < 10:
            return 'shallow'
        elif self.max_depth > 100:
            return 'deep water'
        else:
            return 'mid'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    def category(self):
        if self.weight < 1:
            return 'small'
        elif self.weight > 200:
            return 'large'
        else:
            return 'medium'


class AnimalFactory:
    def create_animal(self, animal_type: str, *args):
        if animal_type.lower() == 'bird':
            return Bird(*args)
        elif animal_type.lower() == 'fish':
            return Fish(*args)
        elif animal_type.lower() == 'mammal':
            return Mammal(*args)
        else:
            raise ValueError('Не соответствует ни одному типу животных')

factory = AnimalFactory()
bird = factory.create_animal('Bird', 'Pyska', 50)
fish = factory.create_animal('Fish', 'Pyska', 50)
mammal = factory.create_animal('mammal', 'Pyska', 50)
print(bird.wing_length())
print(fish.depth())
print(mammal.category())