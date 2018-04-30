import requests, random

url = "http://ibarakaiev.shpp.me/pactf_s7fj43/key_"

s = requests.Session()

for x in range(10000):
	res = s.get("{}{}.txt".format(url, str(x))).text

	if "was not found on this" not in res:
		print("url found : {}.txt".format(url+str(x)))
		break
