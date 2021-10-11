from algorithms.RSA import RSAAlgorithm
from constants import RSA_ENCRYPTED_OUTPUT, BIG_FILE_DIR, RSA_ENCRYPTED_TIME
from file_writer import FileWriter


def encrypt_with_rsa():
    rsa = RSAAlgorithm()
    FileWriter.transform_by_chunk(
        input_path=BIG_FILE_DIR,
        output_path=RSA_ENCRYPTED_OUTPUT,
        parse=rsa.encrypt,
        chunk_size=100,
    )


[measured_time, _] = FileWriter.with_measure_time(encrypt_with_rsa)
FileWriter.write_file(RSA_ENCRYPTED_TIME, str(measured_time))
