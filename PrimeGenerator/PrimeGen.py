class primeGenerator:
    def __init__(self):
        self.prime = 2
    def get(self):
        return self.prime
    def next(self):
        isPrime = False
        while not(isPrime):
            isPrime = True
            self.prime = self.prime + 1
            for i in range(2, self.prime):
                if self.prime % i == 0 :
                    isPrime = False
        