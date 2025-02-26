from abc import ABC, abstractmethod
import time


class Pet(ABC):
    def play(self):
        print("I'm a game being played!")

    def __init__(self, hunger=int, happiness=int, energy=int, name=str):
        self._hunger = hunger
        self._happiness = happiness
        self._energy = energy
        self._name = name

        @property
        def hunger(self):
            return self._hunger

        @hunger.setter
        def hunger(self, hunger):
            if hunger > 0 and hunger < 100:
                self._hunger = hunger
            elif hunger < 0:
                print("Hunger can not be less than 0")
                self._hunger = 0
            elif hunger > 100:
                print("Hunger can not be greater than 100")
                self._hunger = 100

        @property
        def happiness(self):
            return self._happiness

        @happiness.setter
        def happiness(self, happiness):
            if happiness > 0 and happiness < 100:
                self._happiness = happiness
            elif happiness < 0:
                print("Happiness can not be less than 0")
                self._happiness = 0
            elif happiness > 100:
                print("Happiness can not be greater than 100")
                self._happiness = 100

        @property
        def energy(self):
            return self._energy

        @energy.setter
        def energy(self, energy):
            if energy > 0 and energy < 100:
                self._energy = energy
            elif energy < 0:
                print("Energy can not be less than 0")
                self._energy = 0
            elif energy > 100:
                print("Energy can not be greater than 100")
                self._energy = 100

    
    def feed(self):
        self._hunger -= 20
        self._energy += 10

    def play(self):
        self._happiness += 15 
        self._energy -= 10
    
    def sleep(self):
        self._energy += 20 
        self._hunger += 10

    def show_status(self):
        print(f"Hunger: {self._hunger}/100")
        print(f"Energy: {self._energy}/100")
        print(f"Happiness: {self._happiness}/100")

    def random_event(self):
        pass

    @abstractmethod
    def special_ability(self):
        # Each pet must override this method with a unique ability.
        pass


class Dog(Pet):
    def play(self):
        self._happiness += 20 
        self._energy -= 10

    def special_ability(self):
        if self._happiness >= 80:
            print(f"{self._name} used Mega Bark and consumed 10 hunger!")
            self._hunger -= 10
        else:
            print(f"{self._name} does not have enough happiness to use Mega Bark.")


class Cat(Pet):
    def sleep(self):
        self._energy += 30 
        self._hunger += 5

    def special_ability(self):
        if self._happiness <= 20:
            print(f"{self._name} used Nap Time and gained 15 energy!")
            self._energy += 15
        else:
            print(f"{self._name} isn't tired enough to use Nap Time.")


class Dragon(Pet):
    def feed(self):
        self._hunger -= 30 
        self._energy += 15
        self._happiness += 10

    def play(self):
        self._happiness += 25
        self._hunger += 10
        self._energy -= 5

    def special_ability(self):
        if self._happiness >= 70:
            print(f"{self._name} used Flaming Belch and consumed 10 hunger!")
            self._hunger -= 5
            self._energy += 5
        else:
            print(f"{self._name} does not have enough happiness to use Flaming Belch")


def main():
    print("1.Dog🐶")
    print("2.Cat🐱")
    print("3.Dragon🐉")
    pet_type = str(input("Enter the the pet type you want(1-3):"))
    user_in = str(input("WWhat is your pets name?:"))
    while True:
        if pet_type == "1":
            pet = Dog(name = user_in, energy = 50, happiness = 50, hunger = 50)
            break
        elif pet_type == "2":
            pet = Cat(name = user_in, energy = 50, happiness = 50, hunger = 50)
            break
        elif pet_type == "3":
            pet = Dragon(name = user_in, energy = 50, happiness = 50, hunger = 50)
            break
        time.sleep(1)
 
    while True:
        pet.random_event()
        pet.show_status()
        time.sleep(1)
        choice = input(
            '1.Feed \n2.Play \n3.Sleep \n4.Special Ability \n5.Exit \nChoose option: ')
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.special_ability()
        elif choice == '5':
            exit()
        

if __name__ == '__main__':
    main()