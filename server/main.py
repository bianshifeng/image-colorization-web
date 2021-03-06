import os
import flask
import flask_jwt_extended as jwt
from database.seeders import reset_database
from routes import blueprints

# init
app = flask.Flask(__name__)
app.url_map.strict_slashes = False

app.config['JWT_SECRET_KEY'] = os.urandom(256)
jwt.JWTManager(app)


# CLI
@app.cli.command()
def resetdb():
    reset_database()


# index route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return flask.send_file('./static/index.html')


# route for storage, TODO: use nginx instead
@app.route('/api/image/<path:path>')
def get_file_from_storage(path):
    path = '/storage/image_posts/{}'.format(path)
    exts = ['png', 'jpg', 'jpeg']
    for ext in exts:
        if os.path.exists(path + '.' + ext):
            return flask.send_file(path + '.' + ext)

    flask.abort(404)


# modify headers before sending responses
@app.after_request
def map_response(res):
    if os.environ['FLASK_DEBUG'] == '1':
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST, PUT'
    return res


# register blueprints
for bp in blueprints:
    app.register_blueprint(bp)


# start server
if __name__ == '__main__':
    app.run()
