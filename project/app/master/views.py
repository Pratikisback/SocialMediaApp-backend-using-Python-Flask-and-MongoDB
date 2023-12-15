from flask_restful import Api, Resource
from project import api
from flask import make_response, jsonify, request, Blueprint
from project.app.master.controller import insert_post_in_db, insert_many_posts, get_all_posts

post_blueprint = Blueprint("post_blueprint", __name__)


class CreatePost(Resource):
    def post(self):
        try:
            posts = request.json.get("posts", [])
            id = request.json.get("id")
            title = request.json.get("title")
            body = request.json.get("body")
            user_id = request.json.get("userId")
            reactions = request.json.get("reactions", 0)
            tags = request.json.get("tags", [])
            get_posts = request.json.get("get_posts", False)

            if insert_many_posts(posts):
                return make_response(jsonify({"message": "posts inserted successfully"}))

            if user_id:
                if insert_post_in_db(id, title, body, user_id, reactions, tags):
                    return make_response(jsonify({"message": "posted successfully"}))
                else:
                    return make_response(jsonify({"message": "post was not inserted"}))

            elif get_posts:
                data = get_posts()
                return make_response(jsonify({"message": "Posts", "posts": data}))

        except Exception as e:
            return make_response(jsonify({"message": str(e)}))


class GetPosts(Resource):
    def post(self):
        try:
            get_posts = request.json.get("get_posts", False)
            if get_posts:
                data = get_all_posts()
                return make_response(jsonify({"message": "Posts", "posts": data}))

        except Exception as e:
            return make_response(jsonify({"message": str(e)}))


api.add_resource(CreatePost, '/user/create-post')
api.add_resource(GetPosts, '/user/get-posts')
