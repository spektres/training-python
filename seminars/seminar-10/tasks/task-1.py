class AmericanDate:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        self.year = str(self.year)
        return self.year

    def get_month(self):
        self.month = str(self.month)
        return self.month

    def get_day(self):
        self.day = str(self.day)
        return self.day

    def format(self):
        return '{:02}.{:02}.{:04}'.format(self.month, self.day, self.year)

    def set_year(self, y):
        self.year = y

    def set_month(self, m):
        self.month = m

    def set_day(self, d):
        self.day = d

class EuropeanDate:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        self.year = str(self.year)
        return self.year

    def get_month(self):
        self.month = str(self.month)
        return self.month

    def get_day(self):
        self.day = str(self.day)
        return self.day

    def format(self):
        return '{:02}.{:02}.{:04}'.format(self.day, self.month, self.year)

    def set_year(self, y):
        self.year = y

    def set_month(self, m):
        self.month = m

    def set_day(self, d):
        self.day = d

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())