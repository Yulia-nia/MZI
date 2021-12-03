from des import DES
from gost import GOST


def string_to_bin_list(st):
    return [int(i) for i in ''.join('{0:08b}'.format(ord(x), 'b') for x in st)]


def bin_list_to_string(lst):
    if len(lst) % 8:
        zeros = [0 for i in range(8 - len(lst) % 8)]
        lst = zeros + lst
    res = ''
    for i in range(0, len(lst), 8):
        x = 0
        for j in range(i, i + 8):
            x = x * 2 + lst[j]
        res += chr(x)
    return res


def get_double_des(data, KEY1, KEY2):
    des = DES()

    enc1 = des.encrypt(data, KEY1)
    enc2 = des.encrypt(enc1, KEY2)

    dec1 = des.decrypt(enc2, KEY2)
    dec2 = des.decrypt(dec1, KEY1)

    print('KEY1 = {}, KEY2 = {}'.format(bin_list_to_string(KEY1), bin_list_to_string(KEY2)))
    print('Encoded part')
    print('Encoded data with KEY1: {}'.format(bin_list_to_string(enc1)))
    print('Encoded data with KEY2 after encoding with KEY1: {}'.format(bin_list_to_string(enc2)))
    print('Decoded part')
    print('Decoded data with KEY2: {}'.format(bin_list_to_string(dec1)))
    print('Decoded data with KEY1 after decoding with KEY2: {}'.format(bin_list_to_string(dec2)))


def get_triple_des(data, KEY1, KEY2):
    des = DES()

    enc1 = des.encrypt(data, KEY1)
    dec2 = des.decrypt(enc1, KEY2)
    enc1_2 = des.encrypt(dec2, KEY1)

    dec1 = des.decrypt(enc1_2, KEY1)
    enc2 = des.encrypt(dec1, KEY2)
    dec1_2 = des.decrypt(enc2, KEY1)

    print('KEY1 = {}, KEY2 = {}'.format(bin_list_to_string(KEY1), bin_list_to_string(KEY2)))
    print('Encoded part')
    print('Encoded data with KEY1 {}'.format(bin_list_to_string(enc1)))
    print('Decoded data with KEY2 {}'.format(bin_list_to_string(dec2)))
    print('Encoded data with KEY1 after decoding with KEY2 {}'.format(bin_list_to_string(enc1_2)))
    print('Decoded part')
    print('Decoded data with KEY1 {}'.format(bin_list_to_string(dec1)))
    print('Encoded data with KEY2 {}'.format(bin_list_to_string(enc2)))
    print('Decoded data with KEY1 after encoding with KEY2 {}'.format(bin_list_to_string(dec1_2)))


def get_gost(data, KEY3):
    gost = GOST()
    enc = gost.encrypt(data, KEY3)
    dec = gost.decrypt(enc, KEY3)
    print('KEY: {}'.format(bin_list_to_string(KEY3)))
    print('Encoded string: {}'.format(bin_list_to_string(enc)))
    print('Decoded string: {}'.format(bin_list_to_string(dec)))


if __name__ == '__main__':
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    # установка ключей
    KEY1 = 'KSIEH4'
    KEY2 = 'PFEV43'
    KEY3 = 'FKJFLKEJF123456NWNKLQL135676'

    K1 = string_to_bin_list(KEY1)
    K2 = string_to_bin_list(KEY2)
    K3 = string_to_bin_list(KEY3)
    D = string_to_bin_list(data)
    print('-' * 10 + 'DOUBLE DES' + '-' * 10)
    get_double_des(D, K1, K2)

    print('-' * 10 + 'TRIPLE DES' + '-' * 10)
    get_triple_des(D, K1, K2)

    print('-' * 10 + 'GOST' + '-' * 10)
    get_gost(D, K3)

