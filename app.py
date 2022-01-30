
from flask import Flask, request, render_template
import pickle
app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
  return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
  inputQuery1 = request.form['query1']
  inputQuery2 = request.form['query2']
  inputQuery3 = request.form['query3']
  inputQuery4 = request.form['query4']
  inputQuery5 = request.form['query5']
  inputQuery6 = request.form['query6']
  inputQuery7 = request.form['query7']
  inputQuery8 = request.form['query8']
  inputQuery9 = request.form['query9']
  ml_model = pickle.load(open('model.sav', 'rb'))
  data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8, inputQuery9]]
  pred = ml_model.predict(data)
  return render_template('home.html', output1=pred, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'], query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'], query9 = request.form['query9'])


if __name__ == "__main__":
    app.run()
