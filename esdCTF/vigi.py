from pycipher import Vigenere
from itertools import permutations

key = "kabhrfcsu"
ciphertext = "unclyozjeftuojrl"

possibleKeys = permutations(key, 3)

for x in possibleKeys:
	print(''.join(x))
	plaintext = Vigenere(''.join(x)).decipher(ciphertext)
	print(plaintext)


# key = hfa
# flag = NICETOSEEYOUHERE
