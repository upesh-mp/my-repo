class Dog():
    def __init__(self, new_name, start_age):
        self.age = start_age
        self.name = new_name
        self.weight = 0

    def bark(self):
        print("Woof")

# This creates the dog
my_dog = Dog("Spot", 5)

# Print the name to verify it was set
print("I have a dog and he is called" + my_dog.name)

# Call the bark method, format is always object.method()
my_dog.bark()

# Print the name to verify it was set
print("I have a dog and he is" + str(my_dog.age) + "years old")
