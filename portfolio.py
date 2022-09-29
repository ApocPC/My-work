from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Void'

        
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def site():
    return render_template('site.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
