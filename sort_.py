class Rank():
    def __init__(self,code,rate) -> None:
        self.code = code
        self.rate = rate
    
    def __str__(self) -> str:
        return f'{self.code} {self.rate}'

ranks = []
ranks.append(Rank(1,10))
ranks.append(Rank(2,1))
ranks.append(Rank(3,7))
ranks.append(Rank(4,20))

# 不用赋值
ranks.sort(key=lambda x:x.rate, reverse=True)

for rank in ranks:
    print(rank)