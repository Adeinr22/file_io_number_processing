from os import path

class EvenOddExtractor():

    def data_clearer(chosen_file):
        """Clears all data in chosen file"""
        with open(path.join(path.dirname(path.abspath(__file__)), chosen_file), "w"):
            pass

    def data_remover():
        """Remove data in a specific index or range of lines"""
        while True:
            what_to_remove = input('Do you want to remove a data in a specific index (1) or a range of lines (2)? (enter "C" to cancel) \n')
            if what_to_remove == "C" or "c":
                break
            elif what_to_remove == "1":
                while True:
                    index_list = []
                    index_delete = input("Enter the index you want to delete ('N' to stop / 'C' to cancel): ")
                    if index_delete != 'C' or 'c' or 'N' or 'n' or not index_delete.isdigit:
                        print("invalid input")
                    if index_delete == 'C' or 'c':
                        index_list.clear
                        break
                    if index_delete == 'N' or 'n':
                        break
                    else:
                        index_list.append(index_delete)
                if index_list == []:
                    break
                else:
                    pass

            elif what_to_remove == "2":
                pass
            else:
                print("input only 1 or 2")
            pass
        
        
    def random_integer_generator(numbers_to_generate):
        from random import randint
        if numbers_to_generate == 0:
            pass
        elif numbers_to_generate <= 0:
            print("can't go negative")
        elif numbers_to_generate == 1:
            with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                f.write(f"{randint(-1000000, 1000000)}")
        elif numbers_to_generate >= 1:
            with open(path.join(path.dirname(path.abspath(__file__)), "numbers.txt"), "a") as f:
                for i in range(numbers_to_generate):
                    if i == (numbers_to_generate - 1):
                        f.write(f"{randint(-1000000, 1000000)}")
                    else:
                        f.write(f"{randint(-1000000, 1000000)}\n")