import os

class IntegerProcessor:
    """Reads integers.txt, processes even and odd numbers, and writes to double.txt and triple.txt."""

    def __init__(self, filename="integers.txt"):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.input_path = os.path.join(self.base_dir, filename)
        self.double_path = os.path.join(self.base_dir, "double.txt")
        self.triple_path = os.path.join(self.base_dir, "triple.txt")

    def read_integers(self):
        """Reads integers from the input file. Returns a list of integers."""

    def process_and_write(self):
        """Creates double.txt (square of evens) and triple.txt (cube of odds)."""

    def run(self):
        """Main entry point."""

def run_integer_processor():
    """Function called from main.py."""
    processor = IntegerProcessor()
    processor.run()