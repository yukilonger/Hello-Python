class Base():
    def __init__(self) -> None:
        print('init')
    def run(self):
        print('run')
        self.core()
    def core(self):
        print('core')


class Strategy(Base):
    def __init__(self) -> None:
        super().__init__()
        print('init1')
    def core(self):
        print('Strategy')


strategy = Strategy()
strategy.run()