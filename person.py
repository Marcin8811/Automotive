class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print("4elovek sozdan")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " pojot")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " tancujet")

man = Person("Aleks", 30)
woman = Person("Nasty", 28)

man.dance()
woman.dance()
