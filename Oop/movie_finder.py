

class MovieFinder:

    #생성자
    def __init__(self, dao):
        self.dao = dao


    def find_movies(self, kcount, fcount):
        print("DEBUG", "MovieFinder find...")

        movies = self.dao.supply_movies()

        def fn(a, b):
            d1 = a.get_distance(kcount, fcount)
            d2 = b.get_distance(kcount, fcount)

            return d1 - d2

        movies.sort(key=lambda m: m.get_distance(kcount,fcount))

        return movies[0:3]