class Selector:
    def __init__(self, values) -> None:
        self.values = values

    def get_odds(self):
        self.odds_values = []
        for i in self.values:
            if i % 2 != 0:
                self.odds_values.append(i)
        return self.odds_values

    def get_evens(self):
        self.evens_values = []
        for i in self.values:
            if i % 2 == 0:
                self.evens_values.append(i)
        return self.evens_values


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))