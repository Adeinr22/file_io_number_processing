from even_odd_seperator.even_odd_extractor import EvenOddExtractor

while True:
    program_chooser = input("""
MAIN MENU:
    (1) Even and Odd seperator program
    (2) Highest GWA finder
                            
    choose program to run: """)
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
            file_choosed = input("(1) numbers.txt | (2) even.txt | (3) odd.txt | (C) to cancel \nEnter the number for the file you want to remove data from: ")
            if file_choosed == 'C':
                break
            elif file_choosed == 'c':
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
            file_choosed = input("(1) numbers.txt | (2) even.txt | (3) odd.txt | (C) to cancel \nEnter the number for the file you want to remove data from: ")
            if file_choosed == 'C':
                break
            elif file_choosed == 'c':
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
                if numbers_to_generate == 'C':
                    break
                elif int(numbers_to_generate):
                    EvenOddExtractor.random_integer_generator(int(numbers_to_generate))
            except:
                print("Invalid Input")
    
    elif program_1 == '4':
        EvenOddExtractor.even_extractor()

    elif program_1 == '5':
        EvenOddExtractor.odd_extractor()

    elif program_1 == '6':
        EvenOddExtractor.extract_both()

    elif program_1 == 'C':
        break

    else:
        print("invalid input")