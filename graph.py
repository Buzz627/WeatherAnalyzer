import matplotlib.pyplot as plt
from mongoConnection import Connection
import json



colors={"1":"r", "2":"#FFA500", "3":"#FFFF00", "4":"b", "5":"#00FF00"}
# print colors

xCollection="temperature"
yCollection="pressure"
conn=Connection()
for r in sorted(colors.keys()):

	data=conn.findData()({"rating":int(r)}, {xCollection:1, yCollection:1, "precipProbability":1})
	x=[] 
	y=[]
	i=0
	for d in data:
		x.append(d[xCollection])
		y.append(d[yCollection])
		plt.plot(x,y, 'o',color=colors[r], label=r if i==0 else "")
		i+=1
plt.legend(loc='upper center', bbox_to_anchor=(1.06, 1))
plt.xlabel(xCollection.capitalize() +" (deg F)")
plt.ylabel(yCollection.capitalize() +" (mbar)")
plt.title("Weather ratings "+xCollection.capitalize()+" vs "+yCollection.capitalize())
plt.show()
