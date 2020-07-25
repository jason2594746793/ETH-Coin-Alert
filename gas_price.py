class GasPrice:
    def __init__(self, low: float, medium: float, high: float):
        self.low = low
        self.medium = medium
        self.high = high
    def __str__(self):
        return "low: " + str(self.low) + "  medium: " + str(self.medium) + "  high: " + str(self.high) 
