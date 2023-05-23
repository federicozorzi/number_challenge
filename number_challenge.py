import numpy
import random

from useful_function_number_challenge import *

def rand_int(a:int, b:int):
    return random.randint(a, b)

class NumberChallenge:
    def __init__(self, n:int, min_number:int, max_number:int):
        self.n = n
        self.min_number = min_number
        self.max_number = max_number
        self.number_list = numpy.empty(n)
        self.number_list.fill(numpy.NaN)
    
    def __str__(self):
        if numpy.isnan(self.number_list).all():
            return "Game not played yet!"
        else:
            return f"Game ended with status \n {self.number_list}"
    
    def rand_int(self):
        return rand_int(self.min_number,self.max_number)
    
    def simulate_game(self, verbosity:int = 0):
        
        if not numpy.isnan(self.number_list).all():
            print("Game already played")
            return int(not numpy.isnan(self.number_list).any())

        still_alive = 1
        counter = 0

        while still_alive and counter<self.n:
            r = self.rand_int()
            
            pos_start, pos_stop = find_possible_spots(self.number_list, r)

            c = 0
            c, self.number_list = insert_number(self.number_list, r, 
                                                pos_start, pos_stop, 
                                                self.min_number, self.max_number,
                                                verbosity)

            if c==-1:
                still_alive = 0
                if verbosity > 0:
                    print(f"You have lost after {counter} numbers")
                return 0
            else:
                counter = counter + c
                if c==0 and verbosity>2:
                    print(f"Number {r} already extracted: vector is {self.number_list}")
                elif verbosity>2 and c>0:
                    print(f"Number {r} inserted: new vector is {self.number_list}")
                elif verbosity == 2 and c>0:
                    print(f"{r}: {self.number_list}")

        if still_alive == 1:
            if verbosity > 0:
                print(f"You have won! Final list is {self.number_list}")
        return 1
    
    def restart(self):
        self.number_list = numpy.empty(self.n)
        self.number_list.fill(numpy.NaN)


        
