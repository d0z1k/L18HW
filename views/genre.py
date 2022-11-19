from flask_restx import Resource, Namespace

from service.genre import GenreService

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        List all genres.
        """

        return GenreService().get_genres(), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id:int):
        """
        Get a movie by id.
        """

        return "", 200
