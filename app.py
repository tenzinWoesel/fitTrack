from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input')
def input_form():
    return render_template('input_form.html')

@app.route('/dashboard')
def dashboard():
    # Placeholder data for now (replace with actual database queries later)
    activities = [
        {"date": "2024-11-20", "activity": "Running", "duration": 30, "calories": 300},
        {"date": "2024-11-21", "activity": "Cycling", "duration": 60, "calories": 500},
    ]
    return render_template('dashboard.html', activities=activities)

if __name__ == '__main__':
    app.run(debug=True)
