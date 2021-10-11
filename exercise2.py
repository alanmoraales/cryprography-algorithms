from algorithms.AES import AES
from constants import AES_ENCRYPTED_OUTPUT, BIG_FILE_DIR, AES_ENCRYPTED_TIME
from file_writer import FileWriter


with open(BIG_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    [measured_time, encrypted_file] = FileWriter.with_measure_time(
        lambda: AES.encrypt(data_to_encrypt)
    )
    FileWriter.write_file(AES_ENCRYPTED_TIME, str(measured_time))
    FileWriter.write_file(AES_ENCRYPTED_OUTPUT, encrypted_file)
