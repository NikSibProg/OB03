# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        # Инициализация общих атрибутов для всех животных: имя и возраст
        self.name = name
        self.age = age

    def make_sound(self):
        # Метод, который должен быть переопределен в подклассах
        raise NotImplementedError("Метод, который должен быть переопределен в подклассах")

    def eat(self):
        # Общий метод для всех животных, который выводит, что животное ест
        print(f"{self.name} ест.")


# 2. Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        # Вызываем конструктор родительского класса (Animal)
        super().__init__(name, age)
        # Дополнительный атрибут для птиц: размах крыльев
        self.wing_span = wing_span

    def make_sound(self):
        # Переопределение метода для звуков, которые издает птица
        print(f"{self.name} щебечет.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        # Инициализация атрибутов из базового класса
        super().__init__(name, age)
        # Дополнительный атрибут для млекопитающих: цвет меха
        self.fur_color = fur_color

    def make_sound(self):
        # Переопределение метода для звуков млекопитающего
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        # Инициализация атрибутов из базового класса
        super().__init__(name, age)
        # Дополнительный атрибут для рептилий: тип чешуи
        self.scale_type = scale_type

    def make_sound(self):
        # Переопределение метода для звуков, которые издает рептилия
        print(f"{self.name} шипит.")


# 3. Функция для демонстрации полиморфизма
def animal_sound(animals):
    # Принимает список объектов животных и вызывает метод make_sound() для каждого
    for animal in animals:
        animal.make_sound()


# 4. Класс Zoo с композицией
class Zoo:
    def __init__(self):
        # Инициализация пустых списков для хранения животных и сотрудников
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        # Метод для добавления животного в зоопарк
        self.animals.append(animal)
        print(f"Добавляем {animal.name} в зоопарк.")

    def add_employee(self, employee):
        # Метод для добавления сотрудника в зоопарк
        self.employees.append(employee)
        print(f"Добавляем {employee.name} как сотрудника.")

    def feed_all_animals(self):
        # Метод для кормления всех животных в зоопарке
        for employee in self.employees:
            if isinstance(employee, ZooKeeper):
                # Проверяем, является ли сотрудник смотрителем зоопарка
                for animal in self.animals:
                    # Если да, он кормит всех животных
                    employee.feed_animal(animal)

    def heal_all_animals(self):
        # Метод для лечения всех животных в зоопарке
        for employee in self.employees:
            if isinstance(employee, Veterinarian):
                # Проверяем, является ли сотрудник ветеринаром
                for animal in self.animals:
                    # Если да, он лечит всех животных
                    employee.heal_animal(animal)


# 5. Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        # Инициализация имени смотрителя зоопарка
        self.name = name

    def feed_animal(self, animal):
        # Метод для кормления животного, принимает объект животного
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        # Инициализация имени ветеринара
        self.name = name

    def heal_animal(self, animal):
        # Метод для лечения животного, принимает объект животного
        print(f"{self.name} лечит {animal.name}.")



# Пример использования
if __name__ == "__main__":
    # Создаем несколько объектов животных
    parrot = Bird("Попугай", 2, 30)  # Птица, возраст 2, размах крыльев 30 см
    lion = Mammal("Льва", 5, "Золотой")  # Млекопитающее, возраст 5, золотой мех
    snake = Reptile("Змею3", 3, "Гладкая чешуя")  # Рептилия, возраст 3, гладкая чешуя

    # Создаем сотрудников зоопарка
    zookeeper = ZooKeeper("Иван")  # Смотритель по имени Иван
    vet = Veterinarian("Сергей Сергеевич")  # Ветеринар по имени Сергей Сергеевич

    # Создаем объект зоопарка
    zoo = Zoo()

    # Добавляем животных в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Добавляем сотрудников в зоопарк
    zoo.add_employee(zookeeper)
    zoo.add_employee(vet)

    # Вызываем звуки животных через полиморфную функцию
    animal_sound([parrot, lion, snake])

    # Кормим всех животных
    zoo.feed_all_animals()

    # Лечим всех животных
    zoo.heal_all_animals()
