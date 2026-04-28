import os

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

    def read_students(self):
        pass

    def write_students(self):
        pass

    def add_students(self):
        pass

    def remove_students(self):
        pass

    def list_all_students(self):
        pass

    def find_highest_gwa(self):
        pass

    def run(self):
        """Main interactive menu for the Highest GWA program."""
        while True:
            print("""GWA MANAGER: 
(1)  Add a student
(2)  Remove a student
(3)  List all students
(4)  Show student with highest GWA
(5)  Exit to Main Menu""")
            choice = input("\n Choose an option (1-5): ").strip()

            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                print("Returning to main menu...")
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, or 5.")




def run_highest_gwa_program():
    pass