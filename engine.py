import random

class Engine:
    def __init__(self, max_range: int) -> None:
        self.max_range = max_range
        self.number = 0

    def generate_number(self) -> None:
        self.number = random.randint(1, self.max_range)
    
    def try_number(self, number_tried: int) -> str:
        if number_tried > self.number:
            return "lower"
        elif number_tried < self.number:
            return "higher"
        else:
            return "correct"