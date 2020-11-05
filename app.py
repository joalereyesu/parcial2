from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

def reverseString (x):
    reversedString = []
    length = len(x)
    while length > 0:
        reverseString += str[length - 1]
        length = length - 1
    return reverseString



@app.route('/')
def home():
    return render_template('string.html')

@app.route('/crear', methods = ['GET', 'POST'])
def crear():
  if request.method == 'POST':
    _string = request.form['id']
    reverse = reverseString()
    length = len(_string)
    upper = _string.upper()
    print (f'{_string} {reverse} {length}')

    return redirect(url_for('index'))
  template = environment.get_template('done.html')
  return template.render(reverse = reverse, length = length, upper = upper)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)