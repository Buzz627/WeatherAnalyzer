from flask import Flask, send_from_directory, jsonify, request
from saveWeather import save
from weather import getCurrent
from predictKNN import predict
import json


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return send_from_directory(".", "frontEnd.html")

@app.route("/locationTest", methods=['POST'])
def locTest():
	data = request.json
	print(data)
	print(data['latitude'])
	# return "this is working"
	return jsonify({"text":"<a href='https://google.com/maps/place/{d[latitude]},{d[longitude]}'>locationTest</a>".format(d=data)})

@app.route("/rateWeather", methods=['POST'])
def rate():
	data = request.json
	save(data["num"], data)
	return jsonify({"text":"saved"})


@app.route("/current", methods=['POST'])
def current():
	data = request.json
	return jsonify({"text":"<pre>{}\n{}</pre>".format(json.dumps(data, indent=4), json.dumps(getCurrent(data), indent=4))})


@app.route("/predict", methods=['POST'])
def predictCurrent():
	data = request.json
	return jsonify({"text":"<pre>{}</pre>".format(predict(data))})
