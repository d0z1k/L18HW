# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.models import Director


# Например

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        directors = self.session.query(Director).all()
        return directors

    def get_director_by_id(self, id):
        director = self.session.query(Director).filter(Director.id == id).one()
        return director
