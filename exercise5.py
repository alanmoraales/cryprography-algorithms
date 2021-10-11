from algorithms.AES import AESAlgorithm
from constants import AES_DECRYPTED_TIME, AES_DECRYPTED_OUTPUT, BIG_FILE_DIR
from file_writer import FileWriter


aes = AESAlgorithm()

with open(BIG_FILE_DIR, "rb") as file:
    data_to_encrypt = file.read()
    encrypted_file = aes.encrypt(data_to_encrypt)
    [measured_time, decrypted_file] = FileWriter.with_measure_time(
        lambda: aes.desencrypt(encrypted_file)
    )
    FileWriter.write_file(AES_DECRYPTED_TIME, str(measured_time))
    FileWriter.write_file(AES_DECRYPTED_OUTPUT, decrypted_file.decode("utf-8"))
