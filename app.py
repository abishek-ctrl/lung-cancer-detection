from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder='templates')

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        smoking = int(request.form['smoking'])
        yellow_fingers = int(request.form['yellow_fingers'])
        anxiety = int(request.form['anxiety'])
        peer_pressure = int(request.form['peer_pressure'])
        chronic_disease = int(request.form['chronic_disease'])
        fatigue = int(request.form['fatigue'])
        allergy = int(request.form['allergy'])
        wheezing = int(request.form['wheezing'])
        alcohol_consuming = int(request.form['alcohol_consuming'])
        coughing = int(request.form['coughing'])
        shortness_of_breath = int(request.form['shortness_of_breath'])
        swallowing_difficulty = int(request.form['swallowing_difficulty'])
        chest_pain = int(request.form['chest_pain'])
        input_features = [
            [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease,
            fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath,
            swallowing_difficulty, chest_pain]
        ]
        prediction = model.predict(input_features)
        print(prediction)
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
