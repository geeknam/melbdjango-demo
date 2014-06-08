from datetime import datetime

class ComparableMixin(object):

    def __lt__(self, other):
        return self.amount < other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ne__(self, other):
        return self.amount != other.amount


class Price(ComparableMixin):

    def __init__(self, amount):
        self.amount = amount


class Discount(ComparableMixin):

    def __init__(self, amount, expiry_date=None):
        self.amount = amount
        if expiry_date:
            self.expiry_date = expiry_date
        else:
            self.expiry_date = datetime.now()

    @property
    def expired(self):
        return self.expiry_date < datetime.now()



print Price(10.00) < Price(20.00)
print Price(10.00) == Price(10.00)
print Price(10.00) > Price(5.00)
print Price(10.00) != Price(10.00)


print Discount(10.00) < Discount(20.00)
print Discount(10.00) == Discount(10.00)
print Discount(10.00) > Discount(5.00)
print Discount(10.00) != Discount(10.00)