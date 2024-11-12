

class Car:
    def __init__(self, engine, wheels, color):
        self.engine = engine
        self.wheels = wheels
        self.color = color
        
    def start(self):
        print(f"Startuji motor {self.engine}")


c1 = Car(engine="2.0 CRDI", wheels=4, color="Red")
c2 = Car(engine="3.0 TDI", wheels=4, color="Blue")

print(c1.engine, c1.color)

c1.start()