def card(number):
	sum = 0
	num_digits = len(number)
	oddeven = num_digits & 1

	for count in range(0, num_digits):
		digit = int(number[count])

		if not (( count & 1 ) ^ oddeven ):
			digit = digit * 2
		if digit > 9:
			digit = digit - 9

		sum = sum + digit
	return  ((sum % 10) == 0)

f = open("cc_leak.txt.eecc6f896436", 'r')

for x in f:
	if not card(x.strip()):
		print(x.strip())
