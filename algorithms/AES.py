from base64 import b64decode, b64encode
from Crypto.Cipher import AES
import json
import os

aes_key = os.urandom(16)


class AESAlgorithm:
    def encrypt(self, data):
        cipher = AES.new(aes_key, AES.MODE_CTR)
        ciphertext_bytes = cipher.encrypt(data)
        nonce = b64encode(cipher.nonce).decode('utf-8')
        ciphertext = b64encode(ciphertext_bytes).decode('utf-8')
        result = json.dumps({'nonce': nonce, 'ciphertext': ciphertext})
        return result

    def desencrypt(self, data):
        try:
            b64 = json.loads(data)
            nonce = b64decode(b64['nonce'])
            ciphertext = b64decode(b64['ciphertext'])
            cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
            pt = cipher.decrypt(ciphertext)
            return pt
        except ValueError:
            print("Incorrect decryption")
