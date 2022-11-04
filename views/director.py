from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('genre_id')
@director_ns.param('year')
class DirectorsView(Resource):
    def get(self):
        """
        List all Directors.
        """

        return "", 200



@director_ns.route('/<int:director_id>')
class MoviesView(Resource):
    def get(self, director_id:int):
        """
        Get a director by id.
        """

        return "", 200
