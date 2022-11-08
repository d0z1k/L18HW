# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.models import Genre


# Например

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        genres = self.session.query(Genre).all()
        return genres

    def get_director_by_id(self, id):
        genre = self.session.query(Genre).filter(Genre.id == id).one()
        return genre
