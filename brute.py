import itertools
from string import digits, punctuation, ascii_letters
from numba import jit
import time

class Brute:
    def __init__(self):
        self.__password_length = 0
        self.__possible_symbols = None
        self.__pass_2_search = None

    def start(self):
        print("***Hello friend!***")
        try:
            self.__password_length = input("Type possible length of password, for example 3 - 7: ")
            self.__password_length = [int(item) for item in self.__password_length.split("-")]
        except:
            print("Check inputs")

        print("If password contains only digits, type: 1\nIf password contains only letters, type: 2\n"
            "If password contains digits and letters, type: 3\nIf password contains digits, letters and symbols, type: 4")

        try:
            choice = int(input(": "))
            self.set_symbols(choice)
            brutetype = int(input('Do you want to test your password on bruteforce? 1 - No, 2 - Yes: '))
            self.__choose_brute_type(brutetype)
        except Exception as Error:
            print("Error:",Error)

    def __choose_brute_type(self,btype:int):
        if btype == 1:
            self.bruteforce()
        elif btype == 2:
            pass2brute = input('Type your password to test bruteforce time:')
            self.test_brute(pass2brute)
        

    def set_symbols(self, choice:int):
        if choice == 1:
            self.__possible_symbols = digits
        elif choice == 2:
            self.__possible_symbols = ascii_letters
        elif choice == 3:
            self.__possible_symbols = digits + ascii_letters
        elif choice == 4:
            self.__possible_symbols = digits + ascii_letters + punctuation
        else:
            raise ValueError('Choose another value between 1-4')
        
    @jit
    def bruteforce(self):
        for pass_length in range(self.__password_length[0], self.__password_length[1] + 1):
            for password in itertools.product(self.__possible_symbols, repeat=pass_length):
                password = "".join(password)
                print(password)
                if password == self.__pass_2_search:
                    print('Brute forced successfully password:',password)
                    return password
                #return password

    def test_brute(self, word:str):
        self.__pass_2_search = word
        start_time = time.time()
        self.bruteforce()
        print('Time elapsed: %s seconds' % (time.time() - start_time))



if __name__ == '__main__':
    brute = Brute()
    brute.start()
