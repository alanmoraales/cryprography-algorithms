from algorithms.AES import AESAlgorithm
from constants import AES_ENCRYPTED_OUTPUT, AES_DECRYPTED_TIME, AES_DECRYPTED_OUTPUT, ANONYMOUS_FILE_DIR
from with_measure_time import with_measure_time
from write_file import write_file
from base64 import b64decode, b64encode

aes = AESAlgorithm()

with open(ANONYMOUS_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    encrypted_file = aes.encrypt(data_to_encrypt)
    [measured_time, decrypted_file] = with_measure_time(
        lambda: aes.desencrypt(encrypted_file))
    write_file(AES_DECRYPTED_TIME, str(measured_time))
    write_file(AES_DECRYPTED_OUTPUT, decrypted_file.decode('utf-8'))
