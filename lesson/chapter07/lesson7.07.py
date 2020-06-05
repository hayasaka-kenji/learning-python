# プロパティを使った属性の設定
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        # 親クラスの要請
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # 読み込み専用にする
    @property
    def enable_auto_run(self):
        if self.passwd == '456':
            return self._enable_auto_run
        else:
            raise ValueError

    # 書き込み可能にする
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

    def auto_run(self):
        print('auto run')

# tesla_car = TeslaCar('Model S', passwd='456')
# tesla_car.run()
# print(tesla_car.__enable_auto_run)

