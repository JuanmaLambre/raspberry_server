import flask
import json
from libs import filesmanager


app = flask.Flask(__name__)


def response_ok(body):
    return flask.make_response(flask.jsonify(body), 200)

def response_bad_request(message):
    return flask.make_response(flask.jsonify({'message': message}), 400)


@app.route('/ping')
def ping():
    return "Pong!"

@app.route('/files', methods=['GET'])
def files():
    return response_ok({'files': filesmanager.get_files()})

@app.route('/files/<filename>', methods=['GET'])
def file_download(filename):
    if filesmanager.file_exists(filename):
        return flask.send_file(filesmanager.get_path(filename))

@app.route('/files/<filename>', methods=['POST'])
def file_create(filename):
    data = flask.request.get_data()
    if not data:
        return response_bad_request("No files attached")
    else:
        try:
            filesmanager.create_file(filename, data)
        except Exception as e:
            return response_bad_request(e.message)
        return response_ok({'message': 'File {} uploaded'.format(filename)})


@app.route('/files/<filename>', methods=['PUT'])
def file_edit(filename):
    pass
        
@app.route('/files/<filename>', methods=['DELETE'])
def file_delete(filename):
    pass


def main():
    app.run(host='0.0.0.0', port=4804)


if __name__ == "__main__":
    main()
