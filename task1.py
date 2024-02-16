class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")   

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()   

    def swim(self):
        print("moving in water")


shark = Fish()
shark.swim()
shark.breathe()        
