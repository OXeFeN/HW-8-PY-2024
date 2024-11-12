

class Car:
    def __init__(self, engine, wheels, color):
        self.engine = engine
        self.wheels = wheels
        self.color = color
        
    def start(self):
        print(f"Startuji motor {self.engine}")

class House:
    def __init__(self, roof, walls, chimney, windows):
        self.roof = roof
        self.walls = walls
        self.chimney = chimney
        self.windows = windows

    def intruduce(self):
        print(f"My roof is {self.roof}, walls are {self.walls} with {self.windows} windows and {self.chimney} chimney")


c1 = Car(engine="2.0 CRDI", wheels=4, color="Red")
c2 = Car(engine="3.0 TDI", wheels=4, color="Blue")
b1 = House(roof="sloped roof", walls="brick", windows=5, chimney=True)
b2 = House(roof="flat roof", walls="concrete", windows=10, chimney=False)

print(c1.engine, c1.color)

c1.start()

b1.intruduce()
b2.intruduce()