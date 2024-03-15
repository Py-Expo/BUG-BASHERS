from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/disaster')
def disaster():
    return render_template('disaster.html')

@app.route('/partner')
def register():
    return render_template('partner.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/process_donation', methods=['POST'])
def process_donation():
    # Logic to process the donation (e.g., validate form data, handle payment, etc.)
    # Redirect to the success page after processing the donation
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
