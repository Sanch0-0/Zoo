
class Animal:
    def __init__(self, name, age, animal_type, weight, food_type, food_for_feeding):
        self.name = name # Кличка
        self.age = age 
        self._animal_type = animal_type # Млекопитающее \ Репитилия \ Парнокопытное \ Птица
        self._weight = weight # Вес
        self._food_type = food_type # Травоядный \ Плотоядный \ Всеядный
        self._food_for_feeding = food_for_feeding # Мясо \ Рыба \ Злаки
        self._daily_ration = 0.0 # Рацион еды на день(по формуле)

        # Норма прикорма (кг)=Вес животного (кг)×Коэффициент типа животного×Коэффициент рациона

        # Млекопитающее: 0.050.05 (5% от веса)
        # Парнокопытное: 0.080.08 (8% от веса)
        # Рептилия: 0.020.02 (2% от веса)
        # Птица: 0.030.03 (3% от веса)

        # Травоядное: 1.21.2 (увеличенная норма)
        # Плотоядное: 0.80.8 (уменьшенная норма)
        # Всеядное: 1.01.0 (средняя норма)

    def __validate_data(self):
        self.valid_animal_types = [
            'Млекопитающее',
            'Рептилия',
            'Парнокопытное',
            'Птица'
        ]
        self.valid_food_type = [
            'Плотоядное',
            'Травоядное',
            'Всеядное'
        ]

        if self._weight <= 0:
            raise ValueError(f"Неверно указан вес для: {self.name}!")
        elif self.age <= 0:
            raise ValueError(f"Неверно указан возраст для: {self.name}!")

        if self._animal_type not in self.valid_animal_types:
            raise ValueError(f"Задан неверный тип животного для {self.name}!")
        elif self._food_type not in self.valid_food_type:
            raise ValueError(f"Задан неверный образ питания для {self.name}!")

        if self._food_type == "Травоядное":
            self.valid_food_for_feeding = ["Трава", "Фрукты", "Овощи", "Листва"]
        elif self._food_type == "Плотоядное":
            self.valid_food_for_feeding = ["Мясо", "Рыба", "Насекомые"]
        else:
            self.valid_food_for_feeding = [
                "Мясо", "Рыба", "Насекомые",
                "Трава", "Фрукты", "Овощи",
                "Листва", "Злаки", "Орехи",
                "Грибы", "Корни", "Ягоды",
                "Крупы", "Зерна"
            ]

        if self._food_for_feeding not in self.valid_food_for_feeding:
            raise ValueError(f"Задана неверная пища для прикорма для {self.name}!")

    def _calculate_daily_ration(self):
        self.__validate_data()
        animal_type_coefficients = {
            "Млекопитающее": 0.05,
            "Парнокопытное": 0.08,
            "Рептилия": 0.02,
            "Птица": 0.03,
        }
        food_type_coefficients = {
            "Травоядное": 1.2,
            "Плотоядное": 0.8,
            "Всеядное": 1.0,
        }

        animal_type_coefficient = animal_type_coefficients[self._animal_type]
        food_type_coefficient = food_type_coefficients[self._food_type]

        self._daily_ration = self._weight * animal_type_coefficient * food_type_coefficient

        return self._daily_ration

    def make_sound(self):
        return print("Some sounds")

    def show_info(self):
        self.__validate_data() 
        print(f'''
        Кличка: {self.name};
        Возраст: {self.age};
        Вес: {self._weight} кг;
        Тип животного: {self._animal_type};
        Образ питания: {self._food_type};
        Пища для прикорма: {self._food_for_feeding};
        ''')



class Lion(Animal):
    def make_sound(self):
        return print("Roaaaaaar!")

    def hunt(self):
        return print(f"Лев '{self.name}' охотится...")

class Elephant(Animal):
    def make_sound(self):
        return print("Prrrrrrrttttt!")

    def walk(self):
        return print(f"Слон '{self.name}' шагает...")

class Parrot(Animal):
    def make_sound(self):
        return print("Squawk! Squawk!")

    def fly(self):
        return print(f"Попугай '{self.name}' летит...")

class Penguin(Animal):
    def make_sound(self):
        return print("Honk! Honk!")

    def slide(self):
        return print(f"Пингвин '{self.name}' скользит...")

class Crocodile(Animal):
    def make_sound(self):
        return print("Growl... Snap!")

    def swim(self):
        return print(f"Крокодил '{self.name}' плывёт...")

class Snake(Animal):
    def make_sound(self):
        return print("Sssssssss!")

    def crawl(self):
        return print(f"Змея '{self.name}' ползёт...")

class Moose(Animal):
    def make_sound(self):
        return print("Mooooaaaawwwn! ")

    def butt(self):
        return print(f"Лось '{self.name}' бодается...")
