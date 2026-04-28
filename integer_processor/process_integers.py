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
        integers = []
        try:
            with open(self.input_path, "r") as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        num = int(line)
                        integers.append(num)
                    except ValueError:
                        print(f"Warning: Line {line_num} ('{line}') is not an integer. Skipping.")
            if len(integers) == 0:
                print("No valid integers found in the file.")
            elif len(integers) != 20:
                print(f"Note: Expected 20 integers, but found {len(integers)}. Processing anyway.")
        except FileNotFoundError:
            print(f"Error: File '{self.input_path}' not found.")
            print("   Please create 'integers.txt' with 20 integers (one per line).")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []
        return integers
    
    def process_and_write(self, integers):
        """Creates double.txt (square of evens) and triple.txt (cube of odds)."""
        if not integers:
            print("No integers to process. Aborting.")
            return

        evens_squared = []
        odds_cubed = []

        for num in integers:
            if num % 2 == 0:
                evens_squared.append(str(num ** 2))
            else:
                odds_cubed.append(str(num ** 3))

        try:
            with open(self.double_path, "w") as f:
                f.write("\n".join(evens_squared))
            print(f"Written {len(evens_squared)} even squares to {self.double_path}")
        except Exception as e:
            print(f"Error writing double.txt: {e}")

        try:
            with open(self.triple_path, "w") as f:
                f.write("\n".join(odds_cubed))
            print(f"Written {len(odds_cubed)} odd cubes to {self.triple_path}")
        except Exception as e:
            print(f"Error writing triple.txt: {e}")

    def run(self):
        """Main entry point."""

def run_integer_processor():
    """Function called from main.py."""
    processor = IntegerProcessor()
    processor.run()