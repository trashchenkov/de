from flask import Flask, request, render_template
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    request.files['file']
