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
        """Reads all students from the file and returns a list of Student objects."""
        students = []
        try:
            with open(self.filepath, "r") as file:
                for line_num, line in enumerate(file, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    if ',' not in line:
                        raise ValueError(f"Line {line_num}: missing comma separator")
                    name_part, gwa_part = line.split(',', 1)
                    name = name_part.strip()
                    try:
                        gwa = float(gwa_part.strip())
                    except ValueError:
                        raise ValueError(f"Line {line_num}: invalid GWA value '{gwa_part.strip()}'")
                    students.append(Student(name, gwa))
        except FileNotFoundError:
            open(self.filepath, 'a').close()
        except Exception as e:
            print(f"Error reading file: {e}")
        return students

    def write_students(self, students):
        """Writes the list of Student objects back to the file."""
        try:
            with open(self.filepath, "w") as file:
                for student in students:
                    file.write(f"{student.name}, {student.gwa}\n")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def add_students(self, name: str, gwa: float):
        """Adds a new student to the file."""
        students = self.read_students()
        if any(s.name.lower() == name.lower() for s in students):
            print(f"A student named '{name}' already exists. Use a different name or remove the existing one first.")
            return False
        students.append(Student(name, gwa))
        self.write_students(students)
        print(f"Student '{name}' with GWA {gwa} added successfully.")
        return True

    def remove_students(self, name: str):
        """Removes a student by name."""
        students = self.read_students()
        original_count = len(students)
        filtered_students = [s for s in students if s.name.lower() != name.lower()]
        if len(filtered_students) == original_count:
            print(f"No student named '{name}' found.")
            return False
        self.write_students(filtered_students)
        print(f"Student '{name}' removed successfully.")
        return True

    def list_all_students(self):
        """Displays all students with their GWA."""
        students = self.read_students()
        if not students:
            print("No student records found.")
            return
        print("\nAll Students:")
        print("-" * 30)
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. {student.name} → GWA: {student.gwa}")
        print("-" * 30)

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
                name = input("Enter student name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                try:
                    gwa = float(input("Enter GWA (e.g., 1.25): ").strip())
                    if gwa < 1.0 or gwa > 5.0:
                        print("GWA typically ranges from 1.0 (best) to 5.0 (fail). Still saving, but please check.")
                    self.add_students(name, gwa)
                except ValueError:
                    print("Invalid GWA. Please enter a number (e.g., 1.5).")

            elif choice == '2':
                name = input("Enter the exact name of the student to remove: ").strip()
                if name:
                    self.remove_students(name)
                else:
                    print("Name cannot be empty.")

            elif choice == '3':
                self.list_all_students()
                
            elif choice == '4':
                pass
            elif choice == '5':
                print("Returning to main menu...")
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, or 5.")




def run_highest_gwa_program():
    """Entry point called from main.py."""
    finder = HighestGwaFinder()
    finder.run()