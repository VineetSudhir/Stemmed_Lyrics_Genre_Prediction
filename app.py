from flask import Flask, request, render_template
import pickle
import sklearn
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def hello_world():  # put application's code here
    return render_template('genre.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    str_features = [str(x) for x in request.form.values()]
    prediction = model.predict(str_features)

    return render_template('genre.html', pred='The Genre for your lyrics is: ' + prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
