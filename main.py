from flask import Flask, render_template
from form import ContactForm
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def form():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('success.html', form=form)
    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
