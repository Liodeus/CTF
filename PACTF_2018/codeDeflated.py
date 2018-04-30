import os


os.system("zlib-flate -uncompress < uncompress > deflated0")

strg = "deflated"
i = 0
while True:
	res = os.system("zlib-flate -uncompress < {} > {}".format(strg+str(i), strg+str(i+1)))
	if res != 0:
		break
	i += 1

os.system("cat {}".format(strg+str(i)))
os.system("rm deflated*")
