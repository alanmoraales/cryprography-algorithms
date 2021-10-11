from algorithms.RSA import RSAAlgorithm
from constants import RSA_ENCRYPTED_OUTPUT, BIG_FILE_DIR, RSA_ENCRYPTED_TIME
from with_measure_time import with_measure_time
from write_file import write_file

rsa = RSAAlgorithm()
rsa_input = open(BIG_FILE_DIR, mode="rb")
rsa_output = open(RSA_ENCRYPTED_OUTPUT, mode="w", encoding="utf-8")

def write_stuff():
    for data_to_encrypt in rsa_input:
        encrypted_data = rsa.encrypt(data_to_encrypt)
        rsa_output.write(encrypted_data.hex())

rsa_output.close()

[measured_time, _] = with_measure_time(write_stuff)
write_file(RSA_ENCRYPTED_TIME, str(measured_time))
