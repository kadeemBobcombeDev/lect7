import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/') #python decorator
def index():
    num = random.randint(1,20)
    name = 'Kadeem'
    #print("Reached debug statement")
    return flask.render_template(
        "index.html",
        random_number = num, # HTML variable = python variable 
        htmlname = name
    )
    #return "Hello World!"
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)