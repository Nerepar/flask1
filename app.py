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

    if not float(request_data.get('b', 0)):
        return HttpResponse.make(success=False, error_text='Деление на 0')

    del_digits = float(request_data.get('a', 0)) / float(request_data.get('b', 0))
    return HttpResponse.make(data=del_digits)


@app.route('/all_operation', methods=['POST'])
def all_operation():
    request_data = request.get_json() or {}
    a = request_data.get('a', 0)
    b = request_data.get('b', 0)
    return HttpResponse.make(data={
        'sum': a + b,
        'min': a - b,
        'del': a / b,
        'mult': a * b
    })


@app.route('/ct', methods=['POST'])
def checking_text():
    request_data = request.get_json() or {}
    inner_str_one = request_data.get('str_a').lower()
    inner_str_two = request_data.get('str_b').lower()

    if inner_str_two in inner_str_one:
        return HttpResponse.make(data=True)
    else:
        return HttpResponse.make(data=False)


if __name__ == '__main__':
    app.run()
