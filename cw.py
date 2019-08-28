# !! : comments are essential  
def main():
    problem1()
    problem2()
    problem3()

class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
    def printAtts(self):
        print(f'{self.name}, {self.breed}, {self.color}, {self.gender}') # !! : add string formatting to take advantage of f strings 

def problem1():
    ali = Dog("Champ", "boxer", "brown", "male")
    ali.printAtts()

def problem2():
    userin = ""
    while userin != "=":
        userin = input("enter something or press = to  quit  ")

def problem3():
    # !! : indent your code blocks
class Product:
    def __init__(self, name, price, quantity):
         self.name = name
         self.price = price
         self.quantity = quantity
    def changeName(self, newName):
            self.name = newName
    # !! : function to change name and price
    # !! : function to change name, price and quanitity 

sword = Product("Katana", "2900", "1")
# !! : call  your methods on the instance of your class 
main()