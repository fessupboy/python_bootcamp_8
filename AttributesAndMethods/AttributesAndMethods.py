# class Dog():
#
#     # Class object attribute
#     # Same for any instance of a class
#     species = "Mammal"
#
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
#     # Operations/Actions ------> Methods
#     def bark(self,number):
#         print("WOOF My name is {} and the number is {}".format(self.name,number))
#
# my_dog = Dog(breed="Lab", name="Frankie")
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.species)
# my_dog.bark(10)




class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circumfernce(self):
        return self.radius * self.pi * 2

my_circle = Circle(radius=30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfernce())
print(my_circle.area)