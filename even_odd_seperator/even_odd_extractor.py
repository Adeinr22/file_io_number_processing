import os

class EvenOddExtractor():
    def random_integer_generator():
        from random import randint
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "numbers.txt")
        while True:
            try:
                numbers_to_generate = int(input("How many integers you want to generate?\n"))
                with open(file_path, "a") as f:
                    for i in range(numbers_to_generate):
                        if i == (numbers_to_generate - 1):
                            f.write(f"{randint(-1000000, 1000000)}")
                        else:
                            f.write(f"{randint(-1000000, 1000000)}\n")
                break
            except ValueError:
                print("Input must only be an integer")

EvenOddExtractor.random_integer_generator()