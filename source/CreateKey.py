import sympy
import MyMath


def createPQ(): 
    '''
	Trả về 2 giá trị P và Q là 2 số nguyên tố
    '''
    return sympy.randprime(10**300, 10**310), sympy.randprime(10**300, 10**310)


def getE(phi):
    e = 65537
    while MyMath.gcd(e, phi) != 1:
        e += 2
    return e


def getD(e, phi):
    d = MyMath.GCD_extended(e, phi)[0]
    if d < 0:
        d += phi
    return d


def main():
    print("Create Key.....")
    file = open("/Users/danh/Desktop/RSA/data/PrimePQ.txt", mode="w", encoding="utf-8")
    p, q = createPQ()
    file.write(str(p) + "\n" + str(q))
    file.close()
    n = q * p
    phi = (p - 1) * (q - 1)
    e = getE(phi)
    f = open("/Users/danh/Desktop/RSA/data/PublicKey.txt", mode="w", encoding="utf-8")
    f.write(str(n) + "\n" + str(e))
    f.close()

    file = open("/Users/danh/Desktop/RSA/data/PrivateKey.txt", mode="w")
    file.write(str(n) + "\n" + str(getD(e, phi)))
    file.close()
    print("Done!")


main()
