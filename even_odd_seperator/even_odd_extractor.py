from os import path

class EvenOddExtractor():

    def data_clearer(chosen_file):
        """Clears all data in chosen file"""
        with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "w"):
            pass

    def data_remover(chosen_file):
        """Remove data in a specific lines or range of lines"""
        while True:
            what_to_remove = input('Do you want to remove a data in a specific lines (1) or a range of lines (2)? (enter "C" to cancel) \n')
            if what_to_remove.lower() == "c":
                break
            elif what_to_remove == "1":
                while True:
                    line_delete = input("Enter the line you want to delete ('C' to cancel): ")
                    if line_delete.isalpha():
                        if line_delete.lower() == 'c':
                            break
                        else:
                            print("invalid input")
                    elif line_delete.isdigit():
                        lines = []
                        with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "r") as f:
                            all_lines = f.readlines()
                        index = int(line_delete) - 1
                        if 0 <= index < len(all_lines):
                            all_lines.pop(index)
                            with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "w") as f:
                                f.writelines(all_lines)
                    else:
                        print(f"Invalid input. line {line_delete} does not exist. file has {len(all_lines)} lines.")
                    lines.clear()
            elif what_to_remove == "2":
                run_indicator = True
                if run_indicator:
                    while True:
                        start_delete = input("Enter the start of the line you want to delete ('C' to cancel): ")
                        if start_delete.lower() == 'c':
                            run_indicator = False
                            break
                        elif start_delete.isdigit():
                            if int(start_delete) == 0:
                                print("There is no line 0. it starts from line 1")
                            else:
                                break
                        else:
                            print("invalid input")
                if run_indicator:
                    while True:
                        end_delete = input("Enter the end of the line you want to delete ('C' to cancel): ")
                        if end_delete.lower() == 'c':
                            run_indicator = False
                            break
                        elif end_delete.isdigit():
                            if int(start_delete) == int(end_delete):
                                print("starting line and end line must not be the same.")
                            elif int(start_delete) >= int(end_delete):
                                print("ending line number must be higher than the starting line")
                            else:
                                break
                        else:
                            print("invalid input")
                if run_indicator:
                    with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "r") as f:
                        lines = f.readlines()
                    new_lines = [line for idx, line in enumerate(lines, start=1) if not (int(start_delete) <= idx <= int(end_delete))]
                    with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "w") as f:
                        f.writelines(new_lines)               
            else:
                print("Invalid input. Only 1 or 2 or C are allowed")
        
        
    def random_integer_generator(numbers_to_generate):
        """Generate Random Integers based on the user's input"""
        from random import randint
        if numbers_to_generate == 0:
            pass
        elif numbers_to_generate <= 0:
            print("can't go negative")
        elif numbers_to_generate == 1:
            with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                f.write(f"{randint(-1000, 1000)}")
        elif numbers_to_generate >= 1:
            with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                for i in range(numbers_to_generate):
                    if i == (numbers_to_generate - 1):
                        f.write(f"{randint(-1000, 1000)}")
                    else:
                        f.write(f"{randint(-1000, 1000)}\n")