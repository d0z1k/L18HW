from flask_restx import Resource, Namespace

movie_ns = Namespace('movie')


@movie_ns.route('/')
@movie_ns.param('director_id')
@movie_ns.param('genre_id')
@movie_ns.param('year')
class MoviesView(Resource):
    def get(self):
        """
        List all movies.
        """

        return "", 200

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

        return "", 200

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
