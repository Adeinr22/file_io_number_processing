from os import path

class EvenOddExtractor():

    def data_clearer():
        with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "w"):
            pass
        
    def random_integer_generator():
        from random import randint
        while True:
            try:
                numbers_to_generate = int(input("How many integers you want to generate?\n"))
                with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                    for i in range(numbers_to_generate):
                        if i == (numbers_to_generate - 1):
                            f.write(f"{randint(-1000000, 1000000)}")
                        else:
                            f.write(f"{randint(-1000000, 1000000)}\n")
                break
            except ValueError:
                print("Input must only be an integer")

EvenOddExtractor.data_clearer()