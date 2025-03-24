class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there are no elements at all, there is no frequency either
        if not my_list:
            return None
 
        max_frequency = 0
        max_element = None
        for element in my_list:
            frequency = my_list.count(element)
            if not max_element or frequency > max_frequency:
                max_frequency = frequency
                max_element = element
 
        return max_element
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for element in my_list:
            counts[element] = my_list.count(element)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles
    
    def triples(self, my_list:list):
        counts = {}
        for element in my_list:
            counts[element] = my_list.count(element)
 
        triples = 0
        for value in counts.values():
            if value > 2:
                triples += 1
 
        return triples

    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
    #print(ListHelper.triples(numbers))

    find_triples = ListHelper()
    #numbers2 = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(find_triples.triples(numbers))
