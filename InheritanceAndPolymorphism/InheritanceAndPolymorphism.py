class Animal():

    def __init__(self):
        print("Animal Created")
    def whoami(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

# myanimal = Animal()
# myanimal.eat()
# myanimal.whoami()

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def whoami(self):
#         print("I am a dog")
#
#     def bark(self):
#         print("WOOF")
#
#     def eat(self):
#         print("I am a dog and eating")

# mydog = Dog()
# mydog.whoami()
# mydog.eat()
# mydog.bark()


# Polymorphism

class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says Woof"

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says Meow"

# Bog = Dog("Bog")
# Felix = Cat("Felix")
# print(Bog.speak())
# print(Felix.speak())
#
# for pet in [Bog,Felix]:
#     print(type(pet))
#     print(pet.speak())
#
# def pet_speak(pet):
#     print(pet.speak())
#
# pet_speak(Bog)
# pet_speak(Felix)

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " Says woof"

class Cat(Animal):
    def speak(self):
        return self.name + " Says meow"

fido = Dog("Fido")
Isis = Cat("Isis")
print(fido.speak())
print(Isis.speak())