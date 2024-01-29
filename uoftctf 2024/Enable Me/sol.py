def decode_vba(v6, v7, v8):
    v9 = ""
    for i in range(len(v6)):
        xor_char = (chr(v8)[(i % len(chr(v8)))]) + chr(1)
        v9 += chr(v6[i] ^ ord(xor_char[0]))

    v10 = ""
    for i in range(len(v7)):
        xor_char = v9[(i % len(v9))] + chr(1)
        v10 += chr(v7[i] ^ ord(xor_char[0]))

    return v9

v6 = [98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106]
v7 = [44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84]
v8 = 23

decoded_message = decode_vba(v6, v7, v8)
print(decoded_message)
