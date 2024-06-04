from flask import Flask, render_template, request, redirect, url_for
import os

project_root = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(project_root, 'frontend/templates')
app = Flask(__name__, template_folder=template_path)

app.secret_key = "secret_key_app"

from frontend.controllers.patient_controller import *

if __name__ == '__main__':
    
    app.run(debug=True)
