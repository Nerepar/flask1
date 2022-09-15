from flask import Flask, request, make_response

from helpers.HttpResponse import HttpResponse

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '123'


@app.route('/sum', methods=['POST'])
def get_sum():
    request_data = request.get_json() or {}
    sum_digits = int(request_data.get('a', 0)) + int(request_data.get('b', 0))
    return HttpResponse.make(data=sum_digits)


@app.route('/minus', methods=['POST'])
def get_minus():
    request_data = request.get_json() or {}
    minus_digits = int(request_data.get('a', 0)) - int(request_data.get('b', 0))
    return HttpResponse.make(data=minus_digits)


@app.route('/mult', methods=['POST'])
def get_mult():
    request_data = request.get_json() or {}
    multiply_digits = int(request_data.get('a', 0)) * int(request_data.get('b', 0))
    return HttpResponse.make(data=multiply_digits)


@app.route('/del', methods=['POST'])
def get_del():
    request_data = request.get_json() or {}
    del_digits = int(request_data.get('a', 0)) / int(request_data.get('b', 0))
    return HttpResponse.make(data=del_digits)


if __name__ == '__main__':
    app.run()
