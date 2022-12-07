class Balance:

    left_sum = 0
    right_sum = 0

    def add_left(self, kg):
        self.left_sum += int(kg)

    def add_right(self, kg):
        self.right_sum = int(kg)

    def result(self):
        if self.left_sum < self.right_sum:
            return "R"
        elif self.left_sum > self.right_sum:
            return "L"
        else: return "="

balance = Balance()
balance.add_right(15)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
