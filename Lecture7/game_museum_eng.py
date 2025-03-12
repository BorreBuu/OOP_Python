class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year
 
class GameWarehouse:
    def __init__(self):
        self.__games = []
 
    def lisaa_peli(self, game: ComputerGame):
        self.__games.append(game)
 
    def anna_pelit(self):
        return self.__games