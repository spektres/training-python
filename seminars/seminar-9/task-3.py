class Button():

    count = 0

    def click(self):
        Button.count += 1

    def click_count(self):
        return Button.count

    def reset(self):
        Button.count = 0

button = Button()
button.click()
button.click()
print(button.click_count())
button.reset()
button.click()
print(button.click_count())
