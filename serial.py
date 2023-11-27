"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Initialize the serial generator with a starting value.
        """
        self.start = start
        self.increment = 0

    def generate(self):
        """
        Generate the next sequential value and increments the counter.
        """
        self.increment += 1
        return self.start + self.increment - 1
    
    def reset(self):
        """
        Reset the generator to its initial state
        """
        self.increment = 0

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed!")