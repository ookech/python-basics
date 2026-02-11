class Animal: #parent class
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is Moving")

class cat(Animal): #INHERITANCE----acquiring features from other objects  (#child class)

    def sound(self):
        print("cat is meowing")

    def climb(self):
        print("cat is climbing a tree")

class Horse:
    hasTail = True

    def neigh(self):
        print("Horse is neighing")


a = Animal() #OBJECT

c = cat()  #OBJECT

h = Horse()  #OBJECT

#Parent/super/base  class is the class where elements are borrowed from.
#child/sub/derived class is a class who elements are borrowed to.