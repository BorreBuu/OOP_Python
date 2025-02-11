#MOOC.fi decreasing counter:

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        else:
            print("cannot decrease")
    
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original_value

if __name__ == "__main__":
    #counter = DecreasingCounter(10)
    #prints at the beginning stage:
    #counter.print_value()
    # Part 1 The program should always decrese the amount in the self.value stored in the counter by 1
    # 10 -> 9 -> 8 ...
    """ counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value() """
    # Part 2
    """
    counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()"""
    # Part 3
    """ counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value() """
    #Part 4
    counter = DecreasingCounter(55)
    counter.print_value()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()
    counter1 = DecreasingCounter(55)
    counter1.print_value()
    counter1.decrease()
    counter1.print_value()
    counter.print_value()