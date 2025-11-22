from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    team = data.get('team', '')
    prediction = f"{team} va gagner ! 🎯"
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
