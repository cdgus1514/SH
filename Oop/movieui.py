from Oop.movie_dao import MovieDAO
from Oop.movie_finder import MovieFinder


class MovieUI:

    def __init__(self, finder):
        self.finder = finder

    def input(self):
        kcount = int(input("kiss count >> "))
        fcount = int(input("fight count >> "))

        movies = self.finder.find_movies(kcount, fcount)
        print(movies)



if __name__ == "__main__":

    dao = MovieDAO()
    finder = MovieFinder(dao)
    ui = MovieUI(finder)

    ui.input()