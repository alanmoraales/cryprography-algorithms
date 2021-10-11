from constants import RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_TIME, RSA_DECRYPTED_OUTPUT
from algorithms.RSA import RSAAlgorithm
from with_measure_time import with_measure_time
from write_by_chunk import write_by_chunk
from write_file import write_file

def encrypt_with_rsa():
    rsa = RSAAlgorithm()
    write_by_chunk(RSA_ENCRYPTED_OUTPUT, RSA_DECRYPTED_OUTPUT, rsa.desencrypt)
    
[measured_time, _] = with_measure_time(encrypt_with_rsa)
write_file(RSA_DECRYPTED_TIME, str(measured_time))
