class LimitUpMonth():
    def __init__(self) -> None:
        self.month = ''
        self.count = 0
        self.dates = []

    def __str__(self) -> str:
        return f'{self.month[:2]}/{self.month[-2:]} {self.count}'
    
up = LimitUpMonth()
up.month = '2001'
up.count = 1
up1 = LimitUpMonth()
up1.month = '2002'
up1.count = 2

text = []
text.append(str(up))
text.append(str(up1))
print(text)