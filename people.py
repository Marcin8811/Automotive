class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", а вес " + str(self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека : " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

class Warrior(Person):
    """Создаем класс война"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен : " + str(self.rage))

    def description_person(self):
        """Переопределения метода родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)
        # print("Нового война зовут: " + description)
        return description


warrior = Warrior("Conan", 32, 200)
# # warrior.get_rage()
# # warrior.update_weight(150)
# warrior.description_person()
print("Нового война зовут: " + warrior.description_person())
# man = Person("Alex", 30, 180)
# man.description_person()
# # man.weight = 110
# man.update_weight(90)
# man.get_weight()
