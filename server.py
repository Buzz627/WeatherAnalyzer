from flask import Flask, send_from_directory, jsonify, request
import json


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return send_from_directory(".", "location.html")

@app.route("/locationTest", methods=['POST'])
def locTest():
	data = json.loads(request.data)
	print(data)
	print(data['latitude'])
	# return "this is working"
	return "<a href='https://google.com/maps/place/{d[latitude]},{d[longitude]}'>test</a>".format(d=data)

@app.route("/rateWeather", methods=['POST'])
def rate():
	data = json.loads(request.data)
	return json.dumps(data, indent=4)


@app.route("/current", methods=['POST'])
def current():
	data = json.loads(request.data)
	data["path"]="current"
	return json.dumps(data, indent=4)


@app.route("/predict", methods=['POST'])
def predict():
	data = json.loads(request.data)
	data["path"]="predict"
	return json.dumps(data, indent=4)
