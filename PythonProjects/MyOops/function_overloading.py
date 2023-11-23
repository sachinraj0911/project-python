## function overloading
##cat named missy should say "Meow"
##cow named sparta should say "Maaw Maaw"
##cat named HelloKitty should say "Meow"
##dog named tyson should say "woof woof"
##output
##missy: Meow!
##sparta: Maaw Maaw!
##HelloKitty: Meow!
##tyson: woof woof!


class Animal:

    def animalSound(self,a, name):

        if a == "cat" and name == "missy":
            print("missy: Meow!")

        elif a == "cat" and name == "hellokitty":
            print("HelloKitty: Meow!")

        elif a == "caw" and name == "sparta":
            print("sparta: Maaw Maaw!")

        elif a == "dog" and name == "tyson":
            print("tyson: woof woof!")

        else:
            print("none")

obj = Animal()

obj.animalSound("cat", "tyson")


