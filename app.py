# Импорты
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    """Главная страница"""
    return render_template('index.html')


@app.route('/departures/')
def det_departures():
    """Направления"""
    return render_template('departure.html')


@app.route('/tours/')
def get_tours():
    """Туры"""
    return render_template('tour.html')


app.run('0.0.0.0',5000, debug=True)

"""
Распишите роуты, выведите тексты:

– главной /, (выведите здесь будет главная);
– направления /departures/<departure>/ (выведите здесь будет направление);
– тура /tours/<id>/ (выведите здесь будет тур).
 

"""