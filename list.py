sea_creatures = ['shark','octopus','blob fish', 'cuttle fish', 'squid','mantis shimp','anemone']
print (sea_creatures.pop(3))
print (sea_creatures)
del sea_creatures[1]
print (sea_creatures )
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern',
'Arctic']
print(sea_creatures + oceans)
print(sea_creatures * 2)
print(oceans * 3)
sea_creatures = sea_creatures + ['Yeti crab']
print (sea_creatures )

grade = 70
if grade >= 65:
print("Passing grade")

balance = -5
if balance < 0:
print("Balance is below 0, add funds now or you
will be charged a penalty.")

class Shark:
def __init__(self, name):
self.name = name
def swim(self):
print(self.name + " is swimming.")
def be_awesome(self):
print(self.name + " is being awesome.")

class Shark:
animal_type = "fish"
new_shark = Shark()
print(new_shark.animal_type)