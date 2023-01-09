from flask_restx import Resource, Namespace
from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movie')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
@movie_ns.param('director_id')
@movie_ns.param('genre_id')
@movie_ns.param('year')
class MoviesView(Resource):
    def get(self):
        """
        List all movies.
        """

        return movie_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """
        Create a new movie.
        """
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id: int):
        """
        Get a movie by id.
        """

        return movie_schema.dump([movie_service.get_movie_by(movie_id)]), 200

    def put(self, movie_id: int):
        """
        Create a new movie.
        """
        return "", 201

    def __delete__(self, movie_id: int):
        """
        Delete a movie.
        :param movie_id:
        :return:
        """
        return "", 204
