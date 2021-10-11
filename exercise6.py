from constants import RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_TIME, RSA_DECRYPTED_OUTPUT
from algorithms.RSA import RSAAlgorithm
from file_writer import FileWriter


def desencrypt_with_rsa():
    rsa = RSAAlgorithm()
    FileWriter.transform_by_chunk(
        input_path=RSA_ENCRYPTED_OUTPUT,
        output_path=RSA_DECRYPTED_OUTPUT,
        parse=rsa.desencrypt,
        chunk_size=256,
    )


[measured_time, _] = FileWriter.with_measure_time(desencrypt_with_rsa)
FileWriter.write_file(RSA_DECRYPTED_TIME, str(measured_time))
