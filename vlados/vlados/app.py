from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Glavnaia():
    return render_template('avto.html')

@app.route('/svm')
def svm():
    return 'privet'

@app.route('/catalog.html')
def catalog():
    return render_template('catalog.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/testtt.html')
def testtt():
    return render_template('testtt.html')

@app.route('/index.html')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)