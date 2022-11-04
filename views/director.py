from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('genre_id')
@director_ns.param('year')
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


@director_ns.route('/<int:director_id>')
class MoviesView(Resource):
    def get(self, director_id:int):
        """
        Get a director by id.
        """

        return "", 200

    def put(self, director_id:int):
        """
        Create a new director.
        """
        return "", 201

    def __delete__(self, director_id:int):
        """
        Delete a director.
        :param director_id:
        :return:
        """
        return "", 204