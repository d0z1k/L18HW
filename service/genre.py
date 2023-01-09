from typing import List

from dao.genre import GenreDAO
from dao.model.models import Genre


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> List["Genre"]:
        return self.genre_dao.get_all_genres()

    def get_genre_by_id(self, id):
        return self.genre_dao.get_genre_by_id(id)
