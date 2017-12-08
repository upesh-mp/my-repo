class Character():
    def __init__(self, new_name, start_age):
        self.age = start_age
        self.name = new_name
        self.weight = 0

    def talk(self):
        print("I need to make it to the other side of the map")

# This creates the dog
my_Character = Character("Bob", 21)

# Print the name to verify it was set
print("Hi my name is" + my_Character.name)

# Call the bark method, format is always object.method()
my_Character.talk()

# Print the name to verify it was set
print("I am" + str(my_Character.age) + "years old")

