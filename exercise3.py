from algorithms.RSA import RSAAlgorithm
from constants import RSA_ENCRYPTED_OUTPUT, BIG_FILE_DIR, RSA_ENCRYPTED_TIME
from with_measure_time import with_measure_time
from write_file import write_file
from write_line_by_line import write_line_by_line

def encrypt_with_rsa():
    rsa = RSAAlgorithm()
    write_line_by_line(BIG_FILE_DIR, RSA_ENCRYPTED_OUTPUT, rsa.encrypt)
    
[measured_time, _] = with_measure_time(encrypt_with_rsa)
write_file(RSA_ENCRYPTED_TIME, str(measured_time))
