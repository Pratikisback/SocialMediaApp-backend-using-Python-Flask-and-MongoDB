from project import flask_app
from project.app.master.views import post_blueprint

flask_app.register_blueprint(post_blueprint)

if __name__ == "__main__":
    flask_app.run(debug=True, port=5000)