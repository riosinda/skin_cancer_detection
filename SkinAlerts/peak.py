from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('index.html', pages=pages)

@app.route('/about')
def about():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('about.html', pages=pages)

@app.route('/information')
def information():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('information.html', pages=pages)

@app.route('/detection')
def detection():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('detection.html', pages=pages)

@app.route('/database')
def database():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('database.html', pages=pages)

@app.route('/dataprivacy')
def dataprivacy():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('dataprivacy.html', pages=pages)

@app.route('/contact')
def contact():
    pages = [
        '/',
        '/about',
        '/information',
        '/detection',
        '/database',
        '/dataprivacy',
        '/contact']
    
    return render_template('contact.html', pages=pages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)