from cryptography.hazmat.primitives import hashes


def generateMD5Hash(data):
    md5 = hashes.Hash(hashes.MD5())
    md5.update(data)
    return md5.finalize().hex()
