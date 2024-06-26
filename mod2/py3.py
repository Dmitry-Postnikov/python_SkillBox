import sys


def decipher(encrypt: str) -> str:
    result: list = []
    dots: int = 0
    for symbol in encrypt:
        if symbol != '.':
            result.append(symbol)
            dots = 0
            continue
        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0
    return ''.join(result)

if __name__ == '__main__':
    data: str = sys.stdin.read()
    decryption: str = decipher(data)
    print(decryption)