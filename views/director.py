from flask_restx import Resource, Namespace

from dao.model.schema import DirectorSchema
from implemented import director_service

director_ns = Namespace('director')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
@director_ns.param('director_id')
@director_ns.param('genre_id')
@director_ns.param('year')
class DirectorsView(Resource):
    def get(self):
        """
        List all Directors.
        """

        return director_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Get a director by id.
        """

        return director_schema.dump([director_service.get_director_by_id(director_id)]), 200
