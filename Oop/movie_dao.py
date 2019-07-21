from Oop.movie import Movie

class MovieDAO:

    def __init__(self):
        self.movies = [
            Movie("바스터즈", 10, 1, "A"),
            Movie("스파이더맨", 10, 6, "A"),
            Movie("악인전", 16, 1, "A"),
            Movie("벤트", 20, 2, "A"),
            Movie("어벤저스", 13, 5, "A"),
            Movie("101번째 프로포즈", 3, 17, "D"),
            Movie("10일간 원나잇 스탠드", 1, 13, "D"),
            Movie("귀신의향기", 2, 13, "D"),
            Movie("우리 지금 만나", 2, 16, "D"),
        ]

    def supply_movies(self):
        print("DEBUG", "supply_movies")

        return self.movies