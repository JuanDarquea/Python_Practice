"""Object life cylce practice program.
"""

class PartyAnimal:
    """

    """
    def __init__(self, z):
        """

        """
        self.x = 0
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        """

        """
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        """

        """
        print(self.name, 'is destructed')

a = PartyAnimal('Sally')
a.party()

print()
b = PartyAnimal('John')
b.party()

print()
a.party()
b.party()
print()
