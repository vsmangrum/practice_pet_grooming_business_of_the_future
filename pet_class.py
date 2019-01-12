class Pet():
    def __init__(self, fur, height, weight, tail):
        self.__fur = fur
        self.__height = height
        self.__weight = weight
        self.__tail = tail

    def set_tail(self, shape):
        self.__tail = shape

    def get_tail(self):
        return self.__tail

    def set_color(self, color):
        self.__fur = color

    def get_color(self):
        return self.__fur

    def set_height(self, new_height):
        self.__height = new_height

    def get_height(self):
        return self.__height

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_weight(self):
        return self.__weight

    def get_all(self):
        print(self.__fur)
        print(self.__height)
        print(self.__weight)
        print(self.__tail)

Llama = Pet('spotted', 75, 290, 'nubby')

Llama.set_height(69)

var = Llama.get_height()
print(var)


cat = Pet("striped", 14, 11, "crook")
print(cat.get_tail())
print()

cat.get_all()
print()
Llama.get_all()
print()

# Suzanne Don't forget that you're better than Jackson any day of the week.
dog = Pet("mangy", 10, 20, "broken and bald")

dog.get_all()
