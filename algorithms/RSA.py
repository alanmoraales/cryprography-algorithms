from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

private_key = RSA.importKey(open('keys/privkey.pem').read())
public_key = RSA.importKey(open('keys/pubkey.pem').read())


class RSAAlgorithm:

    def encrypt(self, data):
        cipher = PKCS1_v1_5.new(public_key)
        ciphertext = cipher.encrypt(data)
        return ciphertext

    def desencrypt(self, ciphertext):
        sentinel = b"The program failed successfully"
        cipher = PKCS1_v1_5.new(private_key)
        return cipher.decrypt(ciphertext, sentinel, expected_pt_len=0)
