import requests
import json
from binascii import hexlify

def encrypt(pt):
    """Obtain ciphertext (encryption) for plaintext"""
    hex = hexlify(pt.encode()).decode()
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + hex
    r = requests.get(url)
    ct = (json.loads(r.text))["ciphertext"]
    return ct

def main():
    symbols = list("abcdefghijklmnopqrstuvwxyz0123456789{_}ABCDEFGHIJKLMNOPQRSTUVWXYZ !\"#$%&'()*+,-./:;<=>?@[\\]^`|~")
    flag = ''
    for i in range(48):
        messLen = 48 - len(flag) - 1
        mess = "x" * messLen

        ct1 = encrypt(mess)
        for symbol in symbols:
            ct2 = encrypt(mess + flag + symbol)
            if ct1[64:96] == ct2[64:96]:
                flag += symbol
                break

        print(flag)

        if flag[-1] == '}':
            break

main()
