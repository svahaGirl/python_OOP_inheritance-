class Car():
    def __init__(self, modelname, yearm,price):
        self.modelname = modelname
        self.yearm = yearm
        self.price = price

honda = Car('City',2017,100000)
tata = Car('Bolt',2016,500000)

honda.cc=1500

def price_inc(self):
    self.price=(self.price*1.15)

print(honda.__dict__)

