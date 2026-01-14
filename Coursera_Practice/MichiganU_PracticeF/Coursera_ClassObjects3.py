"""Object inheritance practice program.
"""

class PartyAnimal:
    """

    """
    def __init__(self, n):
        """

        """
        self.x = 0
        self.name = n
        print(self.name, 'constructed')

    def party(self):
        """

        """
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
    """

    """
    def __init__(self, n):
        """

        """
        super().__init__(n)
        self.points = 0

    def touchdown(self):
        """

        """
        self.points += 7
        self.party()
        print(self.name, 'touchdown! Points =', self.points)

a = PartyAnimal('Sally')
a.party()

print()
b = FootballFan('John')
b.party()
b.touchdown()

print()
a.party()

print()
b.party()
b.touchdown()
#b.party()

