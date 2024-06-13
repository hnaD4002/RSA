import Convert
import MyMath
import sys
base = 7930

def getKey(file):
    f = open(file, "r")
    n = int(f.readline())
    d = int(f.readline())
    f.close()
    return n, d


def getData(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data


def decode(n, d, cir, path):
    file = open(path, "w")
    fd = open("/Users/danh/Desktop/RSA/data/decode.txt", 'w')
    fs = open("/Users/danh/Desktop/RSA/data/size.txt", "r")
    sizes = list(map(int, fs.read().split()))
    fs.close()
    plain_text = ''
    index = 0

    for size in sizes:
        m_str = cir[index : index + size]
        m = Convert.toPlain(m_str, base)
        fd.write(str(m) + '\n')
        p = MyMath.powMod(m, d, n)
        plain_text += chr(p)
        file.write(chr(p))
        index += size

    file.close()
    return plain_text


def main():
    n, d = getKey("/Users/danh/Desktop/RSA/data/PrivateKey.txt")
    cir = getData("/Users/danh/Desktop/RSA/data/cirpher_text.txt")
    plain = decode(n, d, cir, "/Users/danh/Desktop/RSA/data/plain_text.txt")


if __name__ == "__main__":
    main()
