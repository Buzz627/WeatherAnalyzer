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
	return "https://google.com/maps/place/{d[latitude]},{d[longitude]}".format(d=data)