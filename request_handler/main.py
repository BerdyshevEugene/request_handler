from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/test/')
def save_request():
    data = {'user': request.args.get('user'),
            'id': request.args.get('id'),
            'phone': request.args.get('phone')}
    with open('data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    return 'Success'


if __name__ == '__main__':
    app.run()
