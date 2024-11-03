class Animal():


    def __init__(self, name, age, gender):
        """Инициализация атрибутов человека - имя, возраст, пол"""
        self.name = name
        self.age = age
        self.gender = gender
        print("Cat created")

    def scratchy(self):
        print(self.name + " scratchy")

    def tygydyk_tygydyk(self):
        print(self.name + " tygydyk_tygydyk")

cat = Animal("Jumbo", 12, "boy")

cat.scratchy()
cat.tygydyk_tygydyk()

