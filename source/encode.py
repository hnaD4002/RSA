
import CreateKey
import MyMath
import Convert
base = 7930 # Để mã hoá tiếng việt


def getKey(file):
    f = open(file, "r")
    n = int(f.readline())
    e = int(f.readline())
    f.close()
    return n, e


def getData(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data


def encode(n, e, data, path):
    fe = open("/Users/danh/Desktop/RSA/data/encode.txt", 'w')
    file = open(path, "w")
    fs = open("/Users/danh/Desktop/RSA/data/size.txt", "w")
    cirpher = ''

    for c in data:
        ci = MyMath.powMod(ord(c), e, n)
        fe.write(str(ci) + '\n')
        ci_str = Convert.toCirpher(ci, base)
        fs.write(str(len(ci_str)) + " ")
        cirpher += ci_str
        file.write(ci_str)

    file.close()
    fs.close()
    print(len(cirpher))
    return cirpher


def main():
    n, e = getKey("/Users/danh/Desktop/RSA/data/PublicKey.txt")
    data = getData("/Users/danh/Desktop/RSA/data/data.txt")
    cir = encode(n, e, data, "/Users/danh/Desktop/RSA/data/cirpher_text.txt")


if __name__ == "__main__":
    main()
