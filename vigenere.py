""" Developed by Yu Doudou on 13 November, 2017 """


def encrypt_vigenere(plaintext, keyword):
    ptLen = len(plaintext)
    keyLen = len(keyword)

    quotient = ptLen // keyLen  # 商
    remainder = ptLen % keyLen  # 余

    key = keyword*quotient + keyword[0:remainder]
    ciphertext = ""

    for i in range(0, ptLen):
        if 65 <= ord(plaintext[i]) <= 90:  # upper
            c = int((ord(plaintext[i]) - ord('A') + ord(key[i]) - ord('A')) % 26 + ord('A'))
            ciphertext += chr(c)
        elif 97 <= ord(plaintext[i]) <= 122:  # lower
            c = int((ord(plaintext[i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
            ciphertext += chr(c)
        else:
            ciphertext += plaintext[i]
    print("ENCRYPTED DATA --> ", ciphertext)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    ptLen = len(ciphertext)
    keyLen = len(keyword)

    quotient = ptLen // keyLen
    remainder = ptLen % keyLen
    key = keyword * quotient + keyword[0:remainder]
    plaintext = ""

    for i in range(0, ptLen):
        if 65 <= ord(ciphertext[i]) <= 90:  # upper
            c = int((ord(ciphertext[i]) - ord('A') - ord(key[i]) + ord('A')) % 26 + ord('A'))
            plaintext += chr(c)
        elif 97 <= ord(ciphertext[i]) <= 122:  # lower
            c = int((ord(ciphertext[i]) - ord('a') - ord(key[i]) + ord('a')) % 26 + ord('a'))
            plaintext += chr(c)
        else:
            plaintext += ciphertext[i]
    print("DECRYPTED DATA --> ", plaintext)
    return plaintext


plaintext = input("Please enter plaintext：")
keyword = input("Please enter keyword：")
ciphertext = encrypt_vigenere(plaintext, keyword)
decrypt_vigenere(ciphertext, keyword)
# encrypt_vigenere("ATTACKATDAWN", "LEMON")
# decrypt_vigenere("LXFOPVEFRNHR", "LEMON")