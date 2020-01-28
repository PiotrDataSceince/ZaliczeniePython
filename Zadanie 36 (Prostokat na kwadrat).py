class Prostokat():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def wymiary(self):
        print("Wymiary prostokąta: ", "x = "  ,self.x, " ", "y = "  ,self.y)

class Kwadrat(Prostokat):
    def wymiary(self):
        print("Wymiary prostokąta: ", "x = "  ,self.x, " ", "y = "  ,self.x)
    

