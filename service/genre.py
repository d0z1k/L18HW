from typing import List

from dao.genre import GenreDAO
from dao.movie import MovieDAO


# Пример

class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.movie_dao = genre_dao

    def get_movies(self) -> List["Movie"]:
        return self.movie_dao.get_all_movies()

    def get_movie_by(self, director_id=None, genre_id=None, year=None):

        if director_id is None and genre_id is None and year is None:
            return self.movie_dao.get_movie_by_many_filters(
                director_id=director_id,
                genre_id=genre_id,
                year=year
            )
        if director_id is not None:
            return self.movie_dao.get_movie_by_director_id(director_id)
        elif genre_id is not None:
            return self.movie_dao.get_movie_by_genre_id(genre_id)
        elif year is not None:
            return self.movie_dao.get_movie_by_year(year)
        else:
            return []

    def add_movie(self, data) -> None:
        self.movie_dao.create_movie(**data)

    def update(self, data) -> None:
        self.movie_dao.update_movie(**data)

    def delete(self, id) -> None:
        self.movie_dao.delete_movie(id)
