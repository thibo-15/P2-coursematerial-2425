class Money:
    def __init__(self, amount, currency):
        self.amount = int(amount)
        self.currency = str(currency)

    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float)):  # Controleert of multiplier een getal is
            raise TypeError("Multiplier must be a number")
        return Money(self.amount * multiplier, self.currency)

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"


"""
class Money:
    def __init__(self, amount, currency):
        self.amount = int(amount)
        self.currency = str(currency)

    def __add__(self, other, amount):
        if self.currency == other.currency:
            amount += other.amount
        else: 
            raise ValueError("Can't add different currencies")
        return self.amount + " " + self.currency
        
    def __sub__(self, other, amount):
        if self.currency == other.currency:
            amount -= other.amount
        else: 
            raise ValueError("Can't subtract different currencies")
        return self.amount + " " + self.currency
        
    def __mul__(self, multiplier, amount):
        multiplied = amount * int(multiplier)
        return multiplied + " " + self.currency
        """