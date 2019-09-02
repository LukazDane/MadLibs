# import the Flask class from the flask module
from flask import Flask, render_template, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template("MadLib.html")  # render request template


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)  # render results


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
