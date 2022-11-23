from flask import Flask, render_template, request

app = Flask(__name__)
 
# Function to read in details for page
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
 
@app.route('/')
def homePage():
    name = "Marilu Abrajan Martinez"
    details  = readDetails('static/details.txt')
    return render_template("base.html", name=name, aboutMe=details)
 
@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'
 
@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name = request.form['name']
 
    return render_template('form.html', name=name)
 
if __name__ == '__main__':
    app.run(debug=True)
