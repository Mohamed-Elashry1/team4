class Student:
    def __init__(self, name, age):
        self.__name= name
        self.__age= age
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age= age

s =Student("mohamed",21)
s.set_age(21)
print(s.get_age())

    def get_all_info(self):
        return [self.__name, self.__age]
std1 = Student('mohamed', 20)
print(std1.get_all_info())