import os
import controller
from flask import Flask, render_template
from form import formIndex

SECRET_KEY = os.urandom(32)

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=["POST", "GET"])
def index():
    form = formIndex()
    result = 0
    if form.validate_on_submit():
        if form.measure.data != form.mconverted.data:
            result = controller.tempconverter(int(form.measure.data), int(form.mconverted.data), float(form.numberofdatain.data))
        else:
            result = form.numberofdatain.data
    return render_template('index.html', form=form, result=result)

if __name__ == "__main__":
    app.run()