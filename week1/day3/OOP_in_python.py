#Class and objects

class Dog:
    species = "families"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof"

dog1 = Dog("husky",19)
print(dog1.name)
print(dog1.bark())
print(dog1.species)


#Encapsulation

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self,amount):
        if 0 < amount <=  self.__balance:
            self.__balance -= amount
            return True
        False

account = BankAccount("Bishal",50000)
print(account.get_balance())
account.deposit(5000)
print(account.get_balance())


#Inheritance
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("sub class must implement")

    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def speak(self):
        return f"{self.name} is speaking"

    def wag_tail(self):
        return f"{self.name} is wagging tail"

dog1 = Dog("pug")
print(dog1.speak())

#polymorphism
class Bird:
    def fly(self):
        return "flying in the sky"

class Airplane:
    def fly(self):
        return "flying in the sky"

class Superman:
    def fly(self):
        return "flying in the sky"


def make_it_fly(flying_object):
    print(flying_object.fly())

bird = Bird()
airplane = Airplane()
superman = Superman()

make_it_fly(bird)
make_it_fly(airplane)
make_it_fly(superman)
