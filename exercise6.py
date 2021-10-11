from constants import RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_TIME, RSA_DECRYPTED_OUTPUT
from algorithms.RSA import RSAAlgorithm
from file_writer import FileWriter


def encrypt_with_rsa():
    rsa = RSAAlgorithm()
    FileWriter.transform_by_chunk(
        RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_OUTPUT, rsa.desencrypt
    )


[measured_time, _] = FileWriter.with_measure_time(encrypt_with_rsa)
FileWriter.write_file(RSA_DECRYPTED_TIME, str(measured_time))
