from flask_restx import Resource, Namespace
from dao.model.schema import MovieSchema
from implemented import movie_service
from flask import request

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
# @movie_ns.param('director_id')
# @movie_ns.param('genre_id')
# @movie_ns.param('year')
class MoviesView(Resource):
    def get(self):
        """
        List all movies.
        """

        if director_id := request.args.get("director_id"):
            return movie_schema.dump(movie_service.get_movie_by(director_id=director_id)), 200
        elif genre_id := request.args.get("genre_id"):
            return movie_schema.dump(movie_service.get_movie_by(genre_id=genre_id))
        elif year := request.args.get("year"):
            return movie_schema.dump(movie_service.get_movie_by(year=year))
        else:
            return movie_schema.dump(movie_service.get_movies()), 200

    def post(self):
        """
        Create a new movie.
        """
        movie_service.add_movie(request.json)
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
        Update existing movie data.
        """
        movie_service.update_movie(request.json)
        return "", 201

    def __delete__(self, movie_id: int):
        """
        Delete a movie.
        :param movie_id:
        :return:
        """
        movie_service.delete_movie_by_id(movie_id)
        return "", 204
