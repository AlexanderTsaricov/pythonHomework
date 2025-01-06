# Task 1
from abc import ABC, abstractmethod
import math


class MatrixDimensionError(Exception):
    """Exeption for matrix size mismatch"""
    def __init__(self, message="Размеры матриц не корректны для операции"):
        super().__init__(message)


class Matrix:
    def __init__(self, lists: tuple):
        if any(len(lst) != len(lists[0]) for lst in lists):
            raise AttributeError('Значения длин всех списков должны быть равны')
        self.matrix = [*lists]

    def _getStr(self, li: list):
        """
        Return string from attribute li
        :param li: attribute: a or b or c
        :return: string like are "|a[0|, a[1], a[2]|"
        """
        result = ''
        for i, item in enumerate(li):
            if i == len(li) - 1:
                result += f'{item}|'
            elif i == 0:
                result += f'|{item}, '
            else:
                result += f'{item}, '
        return result

    def _getSum(self, thisList: list, otherList: list):
        """
        Return list from sum this attribute and other attribute
        :param thisList: this attribute
        :param otherList: attribute which needs to  by folder
        :return: list where the sum is the two attributes
        """
        result = []
        for itemThis, itemOther in zip(thisList, otherList):
            result.append(itemThis + itemOther)
        return result

    def _getSub(self, thisList: list, otherList: list):
        """
        Return list from result of subtraction this attribute and other attribute
        :param thisList: this attribute
        :param otherList: attribute which needs to by subtraction
        :return: list where the subtraction is the two attributes
        """
        result = []
        for itemThis, itemOther in zip(thisList, otherList):
            result.append(itemThis - itemOther)
        return result

    def _getSumMul(self, thisList: list, otherList: list):
        """
        Return list from result of multiplication this attribute and other attribute
        :param thisList: this attribute
        :param otherList: attribute which needs to by multiplication
        :return: list where the multiplication is the two attributes and sum his elements
        """
        result = []
        for itemThis, itemOther in zip(thisList, otherList):
            result.append(itemThis * itemOther)
        return sum(result)

    def _get_first_elements(self, index, *lists):
        """
        Return list whith first eelemets
        :param index: index of element from lists, which need take
        :param lists: tuple with lists
        :return: list with first elements from lists
        """
        return [lst[index] for lst in zip(*lists)]
    def getCountRow(self):
        """
        Method return count of rows matrix
        :return: int
        """
        return len(self.matrix)
    def getCountColumn(self):
        """
        Method return count of column matrix
        :return: int
        """
        return len(self.matrix[0])
    def getColumn(self, index):
        """
        Return list of the column matrix
        :param: index number of column
        :return: Return column of index
        """
        resultList = []
        for itemList in self.matrix:
            resultList.append(itemList[index])
        return resultList

    def __str__(self):
        result = ''
        for itemList in self.matrix:
            result += self._getStr(itemList) + '\n'
        return result

    def __len__(self):
        result = 0
        for itemList in self.matrix:
            result += len(itemList)
        return result

    def __add__(self, other):
        if len(self) != len(other):
            raise MatrixDimensionError()
        result = ()
        for itemThis, itemOther in zip(self.matrix, other.matrix):
            sumLists = self._getSum(itemThis, itemOther)
            result += (sumLists, )
        return Matrix(result)

    def __sub__(self, other):
        if len(self) != len(other):
            raise MatrixDimensionError()
        result = ()
        for itemThis, itemOther in zip(self.matrix, other.matrix):
            sumLists = self._getSub(itemThis, itemOther)
            result += (sumLists,)
        return Matrix(result)

    def __mul__(self, other):
        if self.getCountRow() != other.getCountColumn():
            raise MatrixDimensionError()
        result = ()
        for i in range(other.getCountColumn()):
            resultList = []
            for j in range(self.getCountRow()):
                resultList.append(self._getSumMul(self.matrix[i], other.getColumn(j)))
            result += (resultList,)
        return Matrix(result)

    def transpose(self):
        result = ()
        for i in range(self.getCountColumn()):
            result += (self.getColumn(i),)
        return Matrix(result)



def resultTask_1():
    m_1 = Matrix(([1, 2], [5, 2], [1,4]))
    m_2 = Matrix(([1, 2], [3, 2], [1,4]))
    m_3 = Matrix(([2, 3, 4], [2, 3, 4]))
    m_4 = Matrix(([2, 3], [2, 3], [2, 3]))
    m_test = Matrix(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    print(m_1 + m_2)
    print(m_3 * m_4)
    print(m_1.transpose())

# Task 2

class Water:
    def __init__(self):
        self.name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            Storm._Storm__flag = True
            storm = Storm()
            Storm._Storm__flag = False
            return storm
        elif isinstance(other, Fire):
            Steam._Steam__flag = True
            steam = Steam()
            Steam._Steam__flag = False
            return steam
        elif isinstance(other, Earth):
            Dirt._Dirt__flag = True
            dirt = Dirt()
            Earth._Dirt__flag = False
            return dirt
        return None


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            Storm._Storm__flag = True
            storm = Storm()
            Storm._Storm__flag = False
            return storm
        elif isinstance(other, Fire):
            Lightning._Lightning__flag = True
            lightning = Lightning()
            Lightning._Lightning__flag = False
            return lightning
        elif isinstance(other, Earth):
            Dust._Dust__flag = True
            dust = Dust()
            Dust._Dust__flag = False
            return dust
        return None

class Fire:
    def __init__(self):
        self.name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Water):
            Steam._Storm__flag = True
            steam = Steam()
            Steam._Storm__flag = False
            return steam
        elif isinstance(other, Air):
            Lightning._Lightning__flag = True
            lightning = Lightning()
            Lightning._Lightning__flag = False
            return lightning
        elif isinstance(other, Earth):
            Lava._Lava__flag = True
            lava = Lava()
            Lava._Lava__flag = False
            return lava
        return None


class Earth:
    def __init__(self):
       self.name = 'Земля'
    def __add__(self, other):
        if isinstance(other, Water):
            Dirt._Dirt__flag = True
            dirt = Dirt()
            Earth._Dirt__flag = False
            return dirt
        elif isinstance(other, Air):
            Dust._Dust__flag = True
            dust = Dust()
            Dust._Dust__flag = False
            return dust
        elif isinstance(other, Fire):
            Lava._Lava__flag = True
            lava = Lava()
            Lava._Lava__flag = False
            return lava
        return None


class Storm:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Storm.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Воды и Воздуха')
        self.name = 'Шторм'

class Steam:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Steam.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Воды и Огня')
        self.name = 'Пар'

class Dirt:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Dirt.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Воды и Земли')
        self.name = 'Грязь'


class Lightning:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Lightning.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Воздуха и Огня')
        self.name = 'Молния'

class Dust:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Dust.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Воздуха и Земли')
        self.name = 'Пыль'

class Lava:
    __flag = False

    def __init__(self):
        # Метод __init__ не должен быть доступен для создания объектов напрямую
        if not Lava.__flag:
            raise TypeError('Невозможно создать объект Storm напрямую. Используйте сложение Земли и Огня')
        self.name = 'Лава'


# Task 3
class Rectangle:
    def __init__(self, width, height = None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def area(self):
        """
        Method for calculating the area of a rectangle
        :return: int
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method for calculating the perimeter of a rectangle
        :return: int
        """
        return 2 * (self.height + self.width)

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(self.width - other.width, self.height - other.height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

def task_3():
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)
    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect1: {rect1.area()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")
    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")

# Task 4
class Stack:
    def __init__(self, stackData: list):
        self.__stackData = stackData

    def add(self, data):
        self.__stackData.append(data)

    def out(self):
        return self.__stackData.pop(-1)


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def newTask(self, newTask: str, priority: int):
        if self.tasks.get(priority) != None:
            self.tasks[priority] = f'{self.tasks[priority]}\n{newTask}'
        else:
            self.tasks[priority] = newTask
        print(self.tasks)

    def __str__(self):
        sortedList = [None] * len(self.tasks)
        for key, value in self.tasks.items():
            if len(sortedList) - 1 < key:
                sortedList.append(value)
            elif sortedList[key] != None:
                if len(sortedList) - 1 < key + 1:
                    if sortedList[key + 1] == None:
                        sortedList[key + 1] = value
                    else:
                        temp = []
                        for i in range(key + 1, len(sortedList)):
                            temp.append(sortedList[i])
                        for i, item in zip(range(key + 2, len(sortedList) + 1), temp):
                            if i > len(sortedList) - 1:
                                sortedList.append(item)
                            else:
                                sortedList[i] = item
                        sortedList[key + 1] = value
                else:
                    sortedList.append(value)
            else:
                sortedList[key] = value
        resultStr = ''
        for item in sortedList:
            if item != None:
                resultStr += f'{item}\n'
        return resultStr

def task_4():
    manager = TaskManager()
    manager.newTask("сделать уборку", 4)
    manager.newTask("помыть посуду", 4)
    manager.newTask("отдохнуть", 1)
    manager.newTask("поесть", 2)
    manager.newTask("сдать ДЗ", 2)
    print(manager)

# Task 5
class Shape(ABC):
    _pi = 3.14
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def diametr(self):
        return self.rad * 2

    def circumference(self):
        return 2 * self._pi * self.rad

    def area(self):
        return self._pi * (self.rad * self.rad)


class Rectangle_2(Shape):
    def __init__(self, width, height = None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def area(self):
        """
        Method for calculating the area of a rectangle
        :return: int
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method for calculating the perimeter of a rectangle
        :return: int
        """
        return 2 * (self.height + self.width)

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):
        return Rectangle(self.width - other.width, self.height - other.height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

class Triangle(Shape):
    def __init__(self, size_a, size_b, size_c = None):
        self.size_a = size_a
        self.size_b = size_b
        if size_c != None:
            self.size_c = size_c
        else:
            self.size_c = size_b

    def semiperimeter(self):
        return (self.size_a + self.size_b + self.size_c) / 2

    def area(self):
        semiper = self.semiperimeter()
        return math.sqrt(semiper*((semiper - self.size_a) * (semiper - self.size_b) * (semiper - self.size_c)))

# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
# Попытка создания экземпляра абстрактного класса Shape (должновызвать ошибку)
try:
    shape = Shape() # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка: {e}")