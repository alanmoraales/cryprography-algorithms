from algorithms.RSA import RSAAlgorithm
from constants import RSA_ENCRYPTED_OUTPUT, BIG_FILE_DIR, RSA_ENCRYPTED_TIME
from with_measure_time import with_measure_time
from write_file import write_file

rsa = RSAAlgorithm()

with open(BIG_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    data = file.read()
    [measured_time, encrypted_file] = with_measure_time(
        lambda: rsa.encrypt(data_to_encrypt))
    write_file(RSA_ENCRYPTED_TIME, str(measured_time))
    write_file(RSA_ENCRYPTED_OUTPUT, encrypted_file.hex())
