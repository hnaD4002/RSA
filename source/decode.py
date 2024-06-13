import Convert
import MyMath
import sys
import time
import threading

base = 7930


def getKey(file):
    with open(file, "r") as f:
        n = int(f.readline())
        d = int(f.readline())
    return n, d


def getData(path):
    with open(path, "r") as file:
        data = file.read()
    return data


def decode(n, d, cir, path):
    with open(path, "w") as file, open(
        "/Users/danh/Desktop/RSA/data/size.txt", "r"
    ) as fs:
        sizes = list(map(int, fs.read().split()))
        plain_text = ""

        index = 0

        for size in sizes:
            c_str = cir[index : index + size]
            p = Convert.toPlain(c_str, base)
            p = MyMath.powMod(p, d, n)
            p_str = chr(p)
            plain_text += p_str
            file.write(p_str)
            index += size

    print("\nDecoding successful!")
    return plain_text


def main(path, path2):
    n, d = getKey("/Users/danh/Desktop/RSA/data/PrivateKey.txt")
    cir = getData(path2)
    plain = decode(n, d, cir, path)


def print_status():
    dots = 0
    while True:
        time.sleep(1)
        print(f"\rChương trình đang hoạt động{'.' * dots}", end="", flush=True)
        dots = (dots + 1) % 4


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Số lượng đối số không hợp lệ.")
        else:
            status_thread = threading.Thread(target=print_status, daemon=True)
            status_thread.start()
            start = time.time()
            main(sys.argv[1], sys.argv[2])
            end = time.time()
            print(f"\nDecoding time: {end - start:.5f}s")
    except ValueError as e:
        print(f"Error: {e}")
        print("Usages: python3 main.py text.txt")
    finally:
        print("Ends.")
