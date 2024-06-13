def toCirpher(num, base = 128):
	mess = ''
	while num:
		mess += chr(num % base)
		num //= base
	
	mess = mess[::-1]
	return mess


def toPlain(mess, base = 128):
	num = 0
	for c in mess:
		num *= base
		num += ord(c)

	return num


