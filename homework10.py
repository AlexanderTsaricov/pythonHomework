# Task 1
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


