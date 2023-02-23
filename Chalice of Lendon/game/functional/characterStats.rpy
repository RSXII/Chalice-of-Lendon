init python:
        
    class CharacterStats:
        def __init__(self, name, starting_amount):
            self.name = name
            self.amount = starting_amount

        def add(self, amount):
            self.amount += amount

        def subtract(self, amount):
            self.amount -= amount
            if self.amount < 0:
                self.amount = 0

        def __str__(self):
            return str(self.amount)
