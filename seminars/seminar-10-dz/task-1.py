class MinStat:

    min_values = []

    def add_number(self, number):
        self.min_values.append(number)

    def result(self):
        return min(self.min_values)


class MaxStat:

    max_values = []

    def add_number(self, number):
        self.max_values.append(number)

    def result(self):
        return max(self.max_values)


class AverageStat:

    average_values = []

    def add_number(self, number):
        self.average_values.append(number)

    def result(self):
        self.sum_numbers = 0
        for number in self.average_values:
            self.sum_numbers += number
        return self.sum_numbers / len(self.average_values)


values = [-12, -4, 0, 6, 23]

minimum = MinStat()
maximum = MaxStat()
average = AverageStat()
for i in values:
    minimum.add_number(i)
    maximum.add_number(i)
    average.add_number(i)

print(minimum.result(), maximum.result(), '{:<08}'.format(average.result()))
