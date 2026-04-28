from os import path

class Student():
    """Represents a student with a name and GWA."""
    def __init__(self, name: str, gwa: float):
        self.name = name
        self.gwa = gwa

    def __repr__(self):
        return f"student(name='{self.name}', gwa={self.gwa})"
    
class HighestGwaFinder:
    """Reads student data from a file and finds the student with the highest GWA."""
    
    def __init__(self, filename: str = "students.txt"):
        self.filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
