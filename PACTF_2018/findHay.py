import unicodedata

f = open("haystack.ef77fe451087.txt", 'r')
l = ''
for x in f:
	for y in x.split():
		for z in y:
			if ord(z) > 122:
				print(unicodedata.normalize("NFKD", y).encode("ascii", "replace"))
				l += y

print(l)
