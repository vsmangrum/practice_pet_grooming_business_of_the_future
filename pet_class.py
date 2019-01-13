class Pet():
    def __init__(self, fur, height, weight, tail,name):
        self.__fur = fur
        self.__height = height
        self.__weight = weight
        self.__tail = tail
        self.__name = name

    def set_name(self, name):
        self.__tail = name

    def get_name(self):
        return self.__name

    def set_tail(self, shape):
        self.__tail = shape

    def get_tail(self):
        return self.__tail

    def set_color(self, color):
        self.__fur = color

    def get_color(self):
        print(self.__fur)

    def set_height(self, new_height):
        self.__height = new_height

    def get_height(self):
        return self.__height

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_weight(self):
        return self.__weight

    def get_all(self):
        print('===================')
        print(self.__fur)
        print(self.__height)
        print(self.__weight)
        print(self.__tail)
        print(self.__name)
        print('===================')

'''
list_of_aniamls = ['dog', 'cat', 'hamster', 'Llama']


group = [0] * len(list_of_aniamls)
def make_animal_list(list_of_animals,group):

    for x in range(len(list_of_aniamls)):
        for each in list_of_aniamls:
            fur = 'brown'
            height = 10
            weight = 20
            tail = 'teensy nub'
            group[x] = Pet(fur, height, weight, tail, list_of_aniamls[x])

    return group


my_list = make_animal_list(list_of_aniamls, group)

my_list[2].set_color('butterscotch')
my_list[2].get_color()
my_list[2].get_all()

for x in range(len(list_of_aniamls)):
    my_list[x].get_all()
'''



