import time
import sys
import MyMath
import Convert
import threading

base = 7930  # Để mã hoá tiếng việt


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


def writeFile(mess, path):
    file = open(path, "w")
    file.write(mess)
    file.close()
    return None


def print_status():
    dots = 0
    while True:
        time.sleep(1)
        print(f"\rThe program is encoding{'.' * dots}", end="", flush=True)
        dots = (dots + 1) % 4


def encode(n, e, data):
    fs = open("/Users/danh/Desktop/RSA/data/size.txt", "w")
    cirpher = ""

    for c in data:
        ci = MyMath.powMod(ord(c), e, n)
        ci_str = Convert.toCirpher(ci, base)
        fs.write(str(len(ci_str)) + " ")
        cirpher += ci_str

    fs.close()
    print("Encryption successful!!")
    return cirpher


def main(path, path2):
    n, e = getKey("/Users/danh/Desktop/RSA/data/PublicKey.txt")
    data = getData(path2)
    cir = encode(n, e, data)
    writeFile(cir, path)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Số lượng đối số không hợp lệ.")
        else:
            import CreateKey

            status_thread = threading.Thread(target=print_status, daemon=True)
            status_thread.start()
            start = time.time()
            main(sys.argv[1], sys.argv[2])
            end = time.time()
            print(f"Encoding time: {end - start:.5f}s")
    except ValueError as e:
        print(f"Error: {e}")
        print("Usages: python3 main.py cir.txt data.txt")
    finally:
        print("Ends.")
