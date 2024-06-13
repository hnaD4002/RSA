import CreateKey
import MyMath
import Convert
from decode import getData, getKey

base = 7930
n, e = getKey('/Users/danh/Desktop/RSA/data/PublicKey.txt')
n, d = getKey('/Users/danh/Desktop/RSA/data/PrivateKey.txt')
data = getData("/Users/danh/Desktop/RSA/data/data.txt")
fe = open("/Users/danh/Desktop/RSA/data/rsa_cir.txt", 'w')
fd = open("/Users/danh/Desktop/RSA/data/rsa_plain.txt", 'w')
cir = ''
sizes = []


for c in data:
	m = MyMath.powMod(ord(c), e, n)
	m_str = Convert.toCirpher(m, base)
	sizes.append(len(m_str))
	cir += m_str
	fe.write(m_str)


plain = ''
index = 0
for size in sizes:
	c_str = cir[index : index + size]
	p = Convert.toPlain(c_str, base)
	p = MyMath.powMod(p, d, n)
	p_str = chr(p)
	plain += p_str
	fd.write(p_str)
	index += size

print(plain)
fe.close()
fd.close()