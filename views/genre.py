from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')


@genre_ns.route('/')
@genre_ns.param('director_id')
@genre_ns.param('genre_id')
@genre_ns.param('year')
class GenresView(Resource):
    def get(self):
        """
        List all genres.
        """

        return "", 200

    def put(self):
        """
        Create a new genre.
        """
        return "", 201


@genre_ns.route('/<int:genre_id>')
class MoviesView(Resource):
    def get(self, genre_id:int):
        """
        Get a movie by id.
        """

        return "", 200

    def put(self, genre_id:int):
        """
        Create a new genre.
        """
        return "", 201

    def __delete__(self, genre_id:int):
        """
        Delete a genre.
        :param genre_id:
        :return:
        """
        return "", 204