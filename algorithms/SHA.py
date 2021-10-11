from cryptography.hazmat.primitives import hashes


def generateSHA1Hash(data):
    sha1 = hashes.Hash(hashes.SHA1())
    sha1.update(data)
    return sha1.finalize().hex()


def generateSHA2Hash(data):
    sha2 = hashes.Hash(hashes.SHA256())
    sha2.update(data)
    return sha2.finalize().hex()


def generateSHA3Hash(data):
    sha3 = hashes.Hash(hashes.SHA3_256())
    sha3.update(data)
    return sha3.finalize().hex()
