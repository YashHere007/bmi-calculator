function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value) / 100; // Convert cm to meters
    const resultDiv = document.getElementById('result');

    if (isNaN(weight) || isNaN(height)) {
        resultDiv.innerHTML = 'Please enter valid numbers.';
        return;
    }

    if (weight <= 0 || height <= 0) {
        resultDiv.innerHTML = 'Please enter positive values.';
        return;
    }

    const bmi = (weight / (height * height)).toFixed(2);
    let category;

    if (bmi < 18.5) {
        category = 'Underweight';
    } else if (bmi <= 24.9) {
        category = 'Normal Weight';
    } else if (bmi <= 29.9) {
        category = 'Overweight';
    } else if (bmi <= 34.9) {
        category = 'Obese';
    } else if (bmi <= 39.9) {
        category = 'Severely Obese';
    } else {
        category = 'Morbidly Obese';
    }

    resultDiv.innerHTML = `Your BMI: ${bmi}<br>Category: ${category}`;
}