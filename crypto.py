#!/usr/bin/python3

from cryptography.hazmat.backends.openssl.backend import backend as c_openssl
from cryptography.hazmat.primitives import hashes
from binascii import hexlify
import hashlib

def binstr_to_ascii(binstr):
    return hexlify(binstr).decode()


def c_openssl_sha256_hexdigest(data):
    digest = hashes.Hash(hashes.SHA256(), backend=c_openssl)
    digest.update(data.encode())
    bin_str = digest.finalize()
    ascii_str = binstr_to_ascii(bin_str)
    return ascii_str


def python_hashlib_sha256_hexdigest(data):
    m = hashlib.sha256()
    m.update(data.encode())
    bin_str = m.digest()
    ascii_str = binstr_to_ascii(bin_str)
    return ascii_str

test_str = "cat"

print("c_openssl_sha256_hexdigest(", test_str, ") = ",
      c_openssl_sha256_hexdigest(test_str))
print("python_hashlib_sha256_hexdigest(", test_str, ") = ",
      python_hashlib_sha256_hexdigest(test_str))
