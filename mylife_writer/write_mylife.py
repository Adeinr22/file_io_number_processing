import os

class MyLifeWriter:
    """Handles writing multiple lines of text to mylife.txt."""
    def __init__(self, filename="mylife.txt"):
        self.filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    def write_lines(self):
        """Prompts the user for multiple lines and writes them to mylife.txt."""
        print("\nEnter your text (type 'SAVE' on a new line to finish and save):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "SAVE":
                break
            lines.append(line)
        
        try:
            with open(self.filepath, "w") as file:
                for line in lines:
                    file.write(line + "\n")
            print(f"Successfully saved {len(lines)} lines to {self.filepath}")
        except Exception as e:
            print(f"Error writing file: {e}")