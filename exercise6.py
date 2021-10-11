from constants import RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_TIME, RSA_DECRYPTED_OUTPUT
from algorithms.RSA import RSA
from file_writer import FileWriter


def desencrypt_with_rsa():
    FileWriter.transform_by_chunk(
        input_path=RSA_ENCRYPTED_OUTPUT,
        output_path=RSA_DECRYPTED_OUTPUT,
        parse=RSA.desencrypt,
        chunk_size=256,
    )


[measured_time, _] = FileWriter.with_measure_time(desencrypt_with_rsa)
FileWriter.write_file(RSA_DECRYPTED_TIME, str(measured_time))
