# ------------------------------------------------------------------------------/
#   Assignment: Playground
#       Objectives:
#          Get comfortable passing information from the route to the template
#          Understand how to display information passed from the route in the template file
#          Get comfortable with using for loops in the template file
#          Get comfortable with using if statements in the template file
# ------------------------------------------------------------------------------/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi People"

@app.route('/play')
def play():
    return render_template('index.html')

if __name__=="__main__":

    app.run(debug=True)
