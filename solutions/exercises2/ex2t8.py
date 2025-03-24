class Movie:
    def __init__(self, name: str, director: str, genre: str, year: int):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year
 
    def __repr__(self):
        return f"{self.name} ({self.director}), {self.year} - genre: {self.genre}"
 
def movies_of_genre(movies: list, genre: str):
    searched_movies = []
    for movie in movies:
        if movie.genre == genre:
            searched_movies.append(movie)
 
    return searched_movies


if __name__ == "__main__":
    john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986) 
    kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993) 
    jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993) 
    
    movies = [john_woo, kungfu, jet_li, Movie("Hero", "Yimou Zhang", "action", 2002)]  
    
    print("Movies in the action genre:") 
    for movie in movies_of_genre(movies, "action"):  
        print(f"{  movie.director}:  {movie.name}") 