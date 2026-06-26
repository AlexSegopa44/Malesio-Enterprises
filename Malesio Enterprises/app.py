from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible on your local network
    # so you can open it on your phone via your PC's IP address
    app.run(debug=True, host='0.0.0.0', port=5000)