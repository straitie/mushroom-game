class MushroomTest:
    def __init__(self,slots:int,answer:list):
        self.slots = slots
        self.inserted = []
        self.answer = answer
        self.attempts_left = 3
    
    def make_attempt(self):
        if sorted(self.inserted) == sorted(self.answer):
            return True
        else:
            self.attempts_left -= 1
    
    def enter_slot(self, mushroom:str, slot:int):
        if slot <= self.slots and slot > 0:
            self.inserted[slot-1] = mushroom
        else:
            print("invalid slot")