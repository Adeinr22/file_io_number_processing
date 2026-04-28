from even_odd_seperator.even_odd_extractor import EvenOddExtractor
from highest_gwa_finder.find_highest_gwa import run_highest_gwa_program
from mylife_writer.write_mylife import run_mylife_writer
from integer_processor.process_integers import run_integer_processor

def run_even_odd_program():
    """Even and Odd separator submenu."""
    while True:
        program_1 = input("""
MENU:
                      
    (1) Clear Data
    (2) Remove Data
    (3) Generate Integers
    (4) Extract Even Numbers
    (5) Extract Odd Numbers
    (6) Extract Both Even and Odd Numbers
    (C) Cancel
                      
what to do: """)
        print()

        if program_1 == '1':
            while True:
                file_choosed = input("(1) numbers.txt | (2) even.txt | (3) odd.txt | (C) to cancel " \
                "\nEnter the number for the file you want to remove data from: ")
                if file_choosed in ('C', 'c'):
                    break
                elif file_choosed == '1':
                    EvenOddExtractor.data_clearer("numbers.txt")
                elif file_choosed == '2':
                    EvenOddExtractor.data_clearer("even.txt")
                elif file_choosed == '3':
                    EvenOddExtractor.data_clearer("odd.txt")
                else:
                    print('Invalid Input.')

        elif program_1 == '2':
            while True:
                file_choosed = input("(1) numbers.txt | (2) even.txt | (3) odd.txt | (C) to cancel " \
                "\nEnter the number for the file you want to remove data from: ")
                if file_choosed in ('C', 'c'):
                    break
                elif file_choosed == '1':
                    EvenOddExtractor.data_remover("numbers.txt")
                elif file_choosed == '2':
                    EvenOddExtractor.data_remover("even.txt")
                elif file_choosed == '3':
                    EvenOddExtractor.data_remover("odd.txt")
                else:
                    print('Invalid Input.')

        elif program_1 == '3':
            while True:
                numbers_to_generate = input("How many integers you want to generate? ('C' to Cancel)\n")
                try:
                    if numbers_to_generate in ('C', 'c'):
                        break
                    elif int(numbers_to_generate):
                        EvenOddExtractor.random_integer_generator(int(numbers_to_generate))
                        break
                except ValueError:
                    print("Invalid Input")

        elif program_1 == '4':
            EvenOddExtractor.even_extractor()

        elif program_1 == '5':
            EvenOddExtractor.odd_extractor()

        elif program_1 == '6':
            EvenOddExtractor.extract_both()

        elif program_1 in ('C', 'c'):
            break

        else:
            print("invalid input")

while True:
    program_chooser = input("""
MAIN MENU:
    (1) Even and Odd separator program
    (2) Highest GWA finder
    (3) Write to mylife.txt
    (4) Process integers 
    (Q) Quit
                            
Choose program to run: """)

    if program_chooser == '1':
        run_even_odd_program()
    elif program_chooser == '2':
        run_highest_gwa_program()
    elif program_chooser == '3':
        run_mylife_writer()
    elif program_chooser == '4':
        run_integer_processor()
    elif program_chooser in ('Q', 'q'):
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or Q.")