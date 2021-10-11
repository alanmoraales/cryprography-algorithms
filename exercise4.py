from constants import AES_ENCRYPTED_OUTPUT, RSA_ENCRYPTED_OUTPUT
from algorithms.MD5 import generateMD5Hash
from algorithms.SHA import generateSHA1Hash, generateSHA2Hash, generateSHA3Hash

with open(AES_ENCRYPTED_OUTPUT, 'rb') as file:
    file_content = file.read()
    md5Digest = generateMD5Hash(file_content)
    print('AES encrypted md5: ', md5Digest)
    sha1Digest = generateSHA1Hash(file_content)
    print('AES encrypted sha1: ', sha1Digest)
    sha2Digest = generateSHA2Hash(file_content)
    print('AES encrypted sha256: ', sha2Digest)
    sha3Digest = generateSHA3Hash(file_content)
    print('AES encrypted sha3_256: ', sha3Digest)

with open(RSA_ENCRYPTED_OUTPUT, 'rb') as file:
    file_content = file.read()
    md5Digest = generateMD5Hash(file_content)
    print('RSA encrypted md5: ', md5Digest)
    sha1Digest = generateSHA1Hash(file_content)
    print('RSA encrypted sha1: ', sha1Digest)
    sha2Digest = generateSHA2Hash(file_content)
    print('RSA encrypted sha256: ', sha2Digest)
    sha3Digest = generateSHA3Hash(file_content)
    print('RSA encrypted sha3_256: ', sha3Digest)
