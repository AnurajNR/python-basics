#inheritance
class animal:
    def __init__(self,type,breed) -> None:
        self.type=type
        self.breed=breed
    def dora(self): 
        print(self.type,self.breed) 
class cat(animal):
    pass
b=cat("A","Persian")
b.dora()


