from algorithms.MD5 import generateMD5Hash
from algorithms.SHA import generateSHA1Hash, generateSHA2Hash, generateSHA3Hash
from constants import BIG_FILE_DIR

with open(BIG_FILE_DIR, 'rb') as file:
    file_content = file.read()
    md5Digest = generateMD5Hash(file_content)
    print('md5: ', md5Digest)
    sha1Digest = generateSHA1Hash(file_content)
    print('sha1: ', sha1Digest)
    sha2Digest = generateSHA2Hash(file_content)
    print('sha256: ', sha2Digest)
    sha3Digest = generateSHA3Hash(file_content)
    print('sha3_256: ', sha3Digest)
