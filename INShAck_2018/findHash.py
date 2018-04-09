import hashlib

f = open("../wordlist/words.txt", 'r')

salt = "yhbG"
passHash = "f2b31b3a7a7c41093321d0c98c37f5ad"

for x in f:
	hash = hashlib.md5(x.strip() + salt).hexdigest()
	if hash == passHash:
		print(x.strip())
		break
