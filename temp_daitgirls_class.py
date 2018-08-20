class DataItGirls:
    def __init__(self, _name):
        self._name = _name

    def say_something(self, _freq_saying=None):
        if _freq_saying != None:
            self._freq_saying = _freq_saying
            return self._name + ' : ' + self._freq_saying
        else:
            return self._name + ' : 쥬금 x_x'

print('\n')
soryeong = DataItGirls('soryeong')
print(soryeong.say_something())

print('\n')
jinkim = DataItGirls('JinKim')
print(jinkim.say_something(_freq_saying='갈아 넣어요 우리'))

print('\n')
seyomi = DataItGirls('seyomi')
print(seyomi.say_something(_freq_saying='헐 ㄷㅂ'))

print('\n')
alan = DataItGirls('Alan')
print(alan.say_something(_freq_saying='(꾸벅) 안녕하세요 :-)'))
