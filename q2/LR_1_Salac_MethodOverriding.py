class Animal:
    def __init__(self, name:str):
        self.__name = name

    def eat(self):
        pass

    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

class Lion(Animal):
    def __init__(self, name:str):
        super().__init__(name)

    def eat(self):
        print(f"{self._Animal__name} eats fresh meat.")

    def make_sound(self):
        print(f"{self._Animal__name} roars loudly!")

class Elephant(Animal):
    def __init__(self, name:str):
        super().__init__(name)

    def eat(self):
        print(f"{self._Animal__name} eats grass and fruits.")

    def make_sound(self):
        print(f"{self._Animal__name} trumpets!")

class Monkey(Animal):
    def __init__(self, name:str):
        super().__init__(name)

    def eat(self):
        print(f"{self._Animal__name} eats bananas.")

    def make_sound(self):
        print(f"{self._Animal__name} chatters!")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")


lion.make_sound()
lion.eat()
print("-----")
elephant.make_sound()
elephant.eat()
print("-----")
monkey.make_sound()
monkey.eat()
print("-----")