from even_odd_seperator.even_odd_extractor import EvenOddExtractor

while True:

    program_1 = input("""
MENU:
                      
    (1) Clear Data
    (2) Remove Data
    (3) Generate Integers
    (C) Cancel
                      
what to do: """)
    print()
    
    if program_1 == '1':
        while True:
            file_choosed = input("Enter the number for the file you want to clear: (1) numbers.txt | (2) even.txt | (3) odd.txt | (C) to cancel \n")
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

    elif program_1 == 'C':
        break

    else:
        print("invalid input")