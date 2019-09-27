from weather import getCurrent
import json

if __name__=="__main__":
	result=getCurrent()
	print(json.dumps(result, indent=4))