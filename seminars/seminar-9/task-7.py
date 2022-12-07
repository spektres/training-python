class MinMaxWordFinder():

    def __init__(self):
        self.text_list = []

    def add_sentence(self, sentence):
        words = sentence.split()
        self.text_list.extend(words)

    def shortest_words(self):
        minn = self.text_list[0]
        for word in self.text_list:
            if len(word) < len(minn):
                minn = word
            # short_list = []
            # for word in self.text_list:
            # if len(word) == len(minn):
            # short_list.append(word)
        short_list = list(filter(lambda x: len(x) == len(minn), self.text_list))
        return sorted(short_list)


    def longest_words(self):
        maxx = self.text_list[0]
        for word in self.text_list:
            if len(word) > len(maxx):
                maxx = word
        short_list = list(filter(lambda x: len(x) == len(maxx), self.text_list))
        return sorted(list(set(short_list)))


a = MinMaxWordFinder()
a.add_sentence('abc abc ds')
a.add_sentence('sd fd fd nba')
print(a.shortest_words())
print(a.longest_words())
