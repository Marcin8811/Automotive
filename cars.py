class Cars():
    """Создали класс машины"""
    def __init__(self, model, production, engine, price, kilometres, wheels):
        """Инициализируем атрибутов машин"""
        self.model = model
        self.production = production
        self.engine = engine
        self.price = price
        self.kilometres = kilometres
        self.wheels = wheels

    def description_cars(self):
        """Получение описания машин"""
        description = self.model + " producted in " + str(self.production) + " with size of the engine " + str(self.engine) + " in price " + str(self.price) + " has mileage 195.000 km " + "and "+ str(self.wheels) + " wheels."
        return description

    def get_kilometres(self):
        """Получения пробега машины"""
        print("Mileage of our car: " + str(self.kilometres))

    def update_kilometres(self, km):
        """Изменение впробега машины"""
        self.kilometres = km


class Truck(Cars):
    """Создаем класс грузовика, наследующий от Cars"""

    def __init__(self, model, production, engine, price, kilometres, wheels, lifting_capacity):
        """Инициализируем атрибуты класса родителя и добавляем атрибут грузоподъемности"""
        super().__init__(model, production, engine, price, kilometres, wheels)
        self.lifting_capacity = lifting_capacity

    def get_lifting_capacity(self):
        """Получение данных о грузоподъемности"""
        print(f"Lifting capacity of the truck is: {self.lifting_capacity} tons")

    def description_cars(self):
        """Переопределение метода родителя для описания грузовика"""
        description = super().description_cars()  # Получаем описание из родительского класса
        description += f" This truck has a lifting capacity of {self.lifting_capacity} tons."
        return description


# Создаем объект грузовика
truck = Truck("Scania", 2024, 4.0, 100000, 190000, 8, 25)

# Выводим описание нового грузовика
print("Details of new truck are: " + truck.description_cars())

# Получаем информацию о пробеге
truck.get_kilometres()

truck.model = "Volvo"
truck.production = 2023
truck.engine = 3.0
truck.price = 80000
truck.kilometres = 80000
truck.wheels = 12
truck.lifting_capacity = 23

print("Updated details: " + truck.description_cars())
