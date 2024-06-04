from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates')
app.secret_key = "secret_key_app"

from controllers.patient_controller import *

if __name__ == '__main__':
    
    app.run(debug=True)
