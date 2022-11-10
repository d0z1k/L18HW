# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.models import Movie


# Например

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_movie_by_id(self, id):
        movie = self.session.query(Movie).filter(Movie.id == id).one()
        return movie

    def get_movie_by_director_id(self, director_id):
        movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movies

    def get_movie_by_genre_id(self, genre_id):
        movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        return movies

    def get_movie_by_year(self , year):
        movies = self.session.query(Movie).filter(Movie.year == year).all()
        return movies

    def get_movie_by_many_filters(self, **kwargs):
        movie = self.session.query(Movie).filter_by(**kwargs).all()
        return movie

    def create_movie(self, **kwargs):
        try:
            self.session.add(
                Movie(
                    **kwargs
                )
            )
            self.session.commit()
        except Exception as e:
            print(f"не удалось добавить фильм\n{e}")
            self.session.rollback()

    def update_movie(self, **kwargs):
        try:
            self.session.query(Movie.id == kwargs.get("id")).update(
                **kwargs
            )
            self.session.commit()
        except Exception as e:
            print(f"не удалось обновить фильм\n{e}")
            self.session.rollback()

    def delete_movie(self, id):
        try:
            self.session.query(Movie).filter(Movie.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f"не удалось удалить фильм\n{e}")
            self.session.rollback()


