# In this project there are 3 abilities: diving, screaming and eating
# Diving is inherited from the Fish
# Screaming and Eating is inherited from the Animal


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"The {self.__class__.__name__} is eating.")
    
    def scream(self):
        print(f"The {self.__class__.__name__} is screaming.")      
    
class Fish:
    def __init__(self, name):
        self.name = name
    
    def dive(self):
        print(f"The {self.__class__.__name__} is swimming.")

class Dog(Animal):
# Dog inherit its abilities from Animals
# For each of its abilities, there is a specific implementation
    def __init__(self, name):
        super().__init__(name)
    
    def eat(self):
        print(f"The {self.__class__.__name__} devours.")
    
    def scream(self):
        print(f"The {self.__class__.__name__} barks.")      

class Goose(Animal, Fish):
# Goose inherit from Animals and Fish
# For each of its abilities, there is a specific implementation
    def __init__(self, name):
        Animal.__init__(self, name)
        Fish.__init__(self, name)
    
    def dive(self):
        print (f"The {self.__class__.__name__} is diving")

    def eat(self):
        print(f"The {self.__class__.__name__} swallows.")
    
    def scream(self):
        print(f"The {self.__class__.__name__} sungs.") 


class Duck(Goose):
# Duck inherit from Goose. 
# It has the same implementation of dive
    def __init__(self, name):
        Goose.__init__(self, name)
        
    # Its implementation of scream is different from other animals
    def scream(self):
        print(f"The {self.__class__.__name__} quacks.") 

    # For Duck, there is no implementation of eating
    def eat(self):
        raise NotImplementedError("Ducks don't eat in this context.")


# Example usage:
dog = Dog("Rex")
dog.eat()      # Output: The Dog devours.
dog.scream()   # Output: The Dog barks.       

fish = Fish("Red")
fish.dive() # Output: The Fish is swimming.

goose = Goose("Gus")
goose.eat()    # Output: The Goose swallows.  
goose.scream() # Output: The Goose sungs.
goose.dive()   # Output: The Goose is diving.

duck = Duck("Daffy")
try:
    duck.eat()   # This will raise a NotImplementedError
except NotImplementedError as e:
    print(e)     # Output: Ducks don't eat in this context.
duck.dive()    # Output: The Duck is diving.
duck.scream()  # Output: The Duck is quacks