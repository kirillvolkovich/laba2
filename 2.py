def crc32(stroka):
    crc_table = [0] * 256
    polynomial = 0xEDB88320
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        crc_table[i] = crc

    crc = 0xFFFFFFFF
    for byte in stroka:
        crc = crc_table[(crc ^ byte) & 0xFF] ^ (crc >> 8)
    crc ^= 0xFFFFFFFF

    return crc

byte_string = input('Введеите фразу: ').encode()
hash_value = crc32(byte_string)
print("Хэш-значение: ", hash_value)



