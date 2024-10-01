class calculation_class:
    def __init__(self, a, b, ar_operation):
        self.a = a
        self.b = b
        # Stores the arithmetic operation function
        self.ar_operation = ar_operation
        
    def fetch_results(self):
        # Fetches the stored arithmetic operation function with a and b
        return self.ar_operation(self.a, self.b)