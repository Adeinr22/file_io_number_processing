from os import path

class EvenOddExtractor():

    def data_clearer(chosen_file):
        """Clears all data in chosen file"""
        with open(path.join(path.dirname(path.abspath(__file__)), f"{chosen_file}"), "w"):
            pass

    def data_remover():
        pass
        
        
    def random_integer_generator():
        from random import randint
        while True:
            try:
                numbers_to_generate = int(input("How many integers you want to generate?\n"))
                if numbers_to_generate == 0:
                    break
                elif numbers_to_generate <= 0:
                    print("can't go negative")
                elif numbers_to_generate == 1:
                    with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                        f.write(f"{randint(-1000000, 1000000)}")
                    break
                elif numbers_to_generate >= 1:
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
EvenOddExtractor.random_integer_generator()