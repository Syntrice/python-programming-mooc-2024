# Write your solution here:


class Series:

    def __init__(self, title: str, seasons: int, genres: list[str]) -> None:
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self) -> str:
        
        title_string = f"{self.title} ({self.seasons} seasons)\n"
        genre_string = f"genres: {', '.join(self.genres)}\n"
        ratings_string = f"{len(self.ratings)} ratings, average {self.average_rating():.1f} points" if self.ratings else "no ratings"
        
        return (title_string + genre_string + ratings_string)
        
    def rate(self, rating: int):
        
        if not 0 < rating <= 6:
            raise ValueError("ratings must be between 0 and 6.")
        
        self.ratings.append(rating)
        
    def average_rating(self) -> float:
        return sum(self.ratings) / len(self.ratings)

def minimum_grade(rating: float, series_list: list[Series]) -> list[Series]:
    result = []
    for series in series_list:
        if series.average_rating() > rating:
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list[Series]) -> list[Series]:
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
