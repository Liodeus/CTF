import os
import re
import glob

os.system("tar xvf ../42.tar.xz")

while True:
	for x in glob.glob("./*.xz"):
		if "flag" in str(x):
			print("flag")
			print(x)
			os.system("cat {}".format(x))
		num = re.findall("[0-9]+", x)
		os.mkdir(num[0])
		os.system("mv {} {}".format(x, num[0]))

	print("move 1")
	os.chdir("./1")
	os.system("ls")
	os.system("tar xvf ./1.tar.xz")
