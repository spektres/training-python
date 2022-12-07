# class BigBell:

#     def __init__(self):
#         self.world = ''

#     def sound(self):
#         if self.world == '':
#             print("ding")
#             self.world = 'ding'
#         elif self.world == 'ding':
#             print("dong")
#             self.world = 'dong'
#         else: 
#             print('ding')
#             self.world = 'ding'

# bell = BigBell()
# bell.sound()
# bell.sound()
# bell.sound()


class BigBell:

    count = 0

    def __init__(self):
        self.world = 'ding'

    def sound(self):
        if self.count % 2 == 0:
            print("ding")
            self.count += 1
        else: 
            print('dong')
            self.count += 1

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
