def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)


hash = 293366475
f = open("dic.txt", 'r')

for x in f:
	if hash_it(x.strip()) == hash:
		print("The flag is : {}".format(x.strip()))
		break
