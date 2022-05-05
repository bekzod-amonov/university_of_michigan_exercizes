#***************************** Python for Everybody --> Using Databases with Python --> WEEK1 - Object Oriented Python **********************************************

#worked_ex_1
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far so good', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

#worked_ex_2
class PartyAnimal:
    x = 0
    surname = ""
    name = ''

    def __init__(self, z):
        self.surname = z
        print(self.surname, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far so good', self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

b = PartyAnimal('Bekzod')
b.party()
b.party()
b.party()

t = FootballFan('Timur')
#t.party()
t.touchdown()

#***************************** Python for Everybody --> Programming for everybody --> WEEK2 - Basic Structured Query Language *********************************
#***************************** Python for Everybody --> Programming for everybody --> WEEK3 - Data Models and Relational SQL **********************************
#***************************** Python for Everybody --> Programming for everybody --> WEEK4 - Many-to-Many Relationships in SQL *******************************
#***************************** Python for Everybody --> Programming for everybody --> WEEK5 - Databases and Visualization *************************************
