from flask import Flask, render_template

app = Flask(__name__)

category = [
    {"title": 'Одежда', "func_name": 'clothes'},
    {"title": 'Обувь', "func_name": 'shoes'},
    {"title": 'Куртки', "func_name": 'jackets'}
]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jackets/')
def jackets():
    return render_template('jackets.html')


if __name__ == '__main__':
    app.run(debug=True)
