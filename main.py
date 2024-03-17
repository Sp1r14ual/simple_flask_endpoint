from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        # Получаем данные из запроса
        data = request.get_json()

        # Проверяем наличие данных
        if data:
            # Возвращаем приветственное сообщение
            return jsonify({'message': 'Hello World'}), 200
        else:
            return jsonify({'error': 'No data provided'}), 400
    else:
        return jsonify({'error': 'Only POST requests are allowed'}), 405


if __name__ == '__main__':
    app.run(debug=True)
