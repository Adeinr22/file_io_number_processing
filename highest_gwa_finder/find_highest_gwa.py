from os import path

class Student():
    """Represents a student with a name and GWA."""
    def __init__(self, name: str, gwa: float):
        self.name = name
        self.gwa = gwa

    def __repr__(self):
        return f"student(name='{self.name}', gwa={self.gwa})"
    
class StudentRecords:
    """Manages a collection of students and provides queries."""
    def __init__(self, file_path: str):
        self.students = []
        self.load_from_file(file_path)