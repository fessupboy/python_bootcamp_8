class Dog():

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

#my_sample = Sample()
#print(type(my_sample))

my_dog = Dog(breed="Lab", name="Sammy", spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(type(my_dog))