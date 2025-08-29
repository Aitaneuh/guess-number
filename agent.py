class Agent:
    def __init__(self, max_range: int) -> None:
        self.max_range = max_range
        self.low = 1
        self.high = max_range
        self.last_guess = 0

    def generate_guess(self) -> int:
        guess = (self.low + self.high) // 2
        self.last_guess = guess
        return guess

    def update(self, feedback: str) -> None:
        if feedback == "higher":
            self.low = self.last_guess + 1
        elif feedback == "lower":
            self.high = self.last_guess - 1