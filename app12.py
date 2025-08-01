from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_html():
    return render_template('index.html')

@app.route('/menu/emnandilicious.html')
def emnandilicious_menu():
    return render_template('emnandilicious-restaurant.html')

@app.route('/menu/mamagrace.html')
def mama_grace_menu():
    return render_template('mama-grace-kitchen.html')

if __name__ == '__main__':
    app.run(debug=True)
