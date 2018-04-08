import json
from collections import Counter

f = open("file-20171020T1500", 'r')

dicResult = {}
dicCount = {}
dicFinal = {}

for x in f:
	data  = json.loads(x)
	scans = data["scans"]

	for key, value in scans.items():
		try:
			if scans[key]["detected"] == True:
				dicResult[key] += 1
		except:
			dicResult[key] = 1

	for key, value in scans.items():
		try:
			dicCount[key] += 1
		except:
			dicCount[key] = 1

dicFinal = {x:0 for x, y in dicCount.items()}

for key, value in dicCount.items():
	dicFinal[key] = (dicResult[key] / value) * 100

print(Counter(dicFinal))
# flag is the 5 first antivirus engines
