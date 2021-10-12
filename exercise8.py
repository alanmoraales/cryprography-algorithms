from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from constants import AES_ENCRYPTED_OUTPUT

with open(AES_ENCRYPTED_OUTPUT, "rb") as file:
    data_to_sign = file.read()
    private_key = ec.generate_private_key(ec.SECP384R1())
    print("Generating signature")
    signature = private_key.sign(data_to_sign, ec.ECDSA(hashes.SHA256()))
    public_key = private_key.public_key()
    try:
        print("verifying signature")
        public_key.verify(signature, data_to_sign, ec.ECDSA(hashes.SHA256()))
        print("The signature is valid :)")
    except InvalidSignature:
        print("The signature is invalid :C")
