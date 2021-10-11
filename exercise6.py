from constants import RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_TIME, RSA_DECRYPTED_OUTPUT, BIG_FILE_DIR
from algorithms.RSA import RSAAlgorithm
from with_measure_time import with_measure_time
from write_file import write_file

rsa = RSAAlgorithm()

with open(BIG_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    encrypted_file = rsa.encrypt(data_to_encrypt)
    [measured_time, decrypted_file] = with_measure_time(
        lambda: rsa.desencrypt(encrypted_file))
    write_file(RSA_DECRYPTED_TIME, str(measured_time))
    write_file(RSA_DECRYPTED_OUTPUT, decrypted_file.decode('utf-8'))
