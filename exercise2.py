from algorithms.AES import AESAlgorithm
from constants import AES_ENCRYPTED_OUTPUT, BIG_FILE_DIR, AES_ENCRYPTED_TIME
from with_measure_time import with_measure_time
from write_file import write_file

aes = AESAlgorithm()

with open(BIG_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    [measured_time, encrypted_file] = with_measure_time(
        lambda: aes.encrypt(data_to_encrypt))
    write_file(AES_ENCRYPTED_TIME, str(measured_time))
    write_file(AES_ENCRYPTED_OUTPUT, encrypted_file)
