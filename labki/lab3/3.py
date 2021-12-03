import math
import random
from sympy import *


def prime_number():
    while True:
        number = random.randrange(10, 1000)
        if isprime(number):
            break
    return number


def e_create(euler_function):
    for e in range(3, euler_function, 2):
        if math.gcd(e, euler_function) == 1:
            return e


def d_create(euler_function, e):
    for d in range(1, euler_function, 1):
        if (d * e) % euler_function == 1:
            return d


def rsa_encrypt(input_data, M, e, n):
    if not (M < n):
        print('Error')
        return None
    if isinstance(input_data, str):
        input_data = [ord(item) for item in input_data]
    result_data = []
    for byte in input_data:
        C = (byte ** e) % n
        result_data.append(C)
    return result_data


def rsa_decrypt(input_data, d, n):
    result_data = []
    for byte in input_data:
        M = (byte ** d) % n
        result_data.append(chr(M))
    return ''.join(result_data)


def keys():
    p = prime_number()
    q = prime_number()
    n = p * q
    euler_function = (p - 1) * (q - 1)
    print('p: {}, q: {}'.format(p, q))
    print('n: {}\neuler_function: {}'.format(n, euler_function))
    return p, q, n, euler_function


if __name__ == '__main__':
    file = open("data.txt", "r")
    data = file.read()
    file.close()

    p, q, n, euler_function = keys()
    e = e_create(euler_function)
    print('d')
    d = d_create(euler_function, e)
    print('e: {}, d: {}'.format(e, d))

    encrypted_data = rsa_encrypt(data, euler_function, e, n)
    print("\nEncrypted data:\n" + str(encrypted_data))

    decrypted_data = rsa_decrypt(encrypted_data, d, n)
    print("Decrypted data:\n" + str(decrypted_data))
