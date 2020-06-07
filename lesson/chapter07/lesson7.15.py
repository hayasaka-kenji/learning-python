# 特殊メソッド

class Word(object):

    def __init__(self, text):
        self.text = text

    # 文字列として扱おうとしたときのメソッド
    def __str__(self):
        return 'word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return  self.text.lower() == word.text.lower()


w = Word('test')
print(w)
# word!!!!
w2 = Word('test')

print(w == w2)