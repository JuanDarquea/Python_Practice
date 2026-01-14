"""
Obeject Oriented Program (OOP) practice.
"""

class PartyAnimal:
    """

    """
    def __init__(self):
        """

        """
        self.x = 0
        print('I am constructed')

    def party(self):
        """

        """
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        """

        """
        print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
#print('Type an ->', type(an))
#print('Dir an ->', dir(an))
#print('Type x ->', type(an.x))
#print('Type party ->', type(an.party))
an = 42
print()
print('an contains', an)

print()
an = PartyAnimal()
try:
    an.party()
except Exception as e:
    print('Error:', e)

an = 50
print()
print('an contains', an)
