from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    # BMI = weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obese"
    elif 35 <= bmi <= 39.9:
        return "Severely Obese"
    else:
        return "Morbidly Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100  # Convert cm to meters
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                category = get_bmi_category(bmi)
            else:
                category = "Please enter valid positive values."
        except ValueError:
            category = "Please enter valid numbers."
    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)