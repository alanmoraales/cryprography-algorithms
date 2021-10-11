from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA as Crypto_RSA

private_key = Crypto_RSA.importKey(open("keys/privkey.pem").read())
public_key = Crypto_RSA.importKey(open("keys/pubkey.pem").read())


class RSA:
    @staticmethod
    def encrypt(data):
        cipher = PKCS1_v1_5.new(public_key)
        ciphertext = cipher.encrypt(data)
        return ciphertext

    @staticmethod
    def desencrypt(ciphertext):
        sentinel = b"The program failed successfully"
        cipher = PKCS1_v1_5.new(private_key)
        return cipher.decrypt(ciphertext, sentinel, expected_pt_len=0)
