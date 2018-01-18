# Casare Algorithm

def convert(c, key, start = 'a', n = 26):
    a = ord(start)
    offset = ((ord(c) - a + key)%n)
    return chr(a + offset)

def encrypt_caesar(plaintext,key):
    """
      Encrypts plaintext using a Caesar cipher.

      >>> encrypt_caesar("PYTHON", 3)
      'SBWKRQ'
      >>> encrypt_caesar("python", 3)
      'sbwkrq'
      >>> encrypt_caesar("Python3.6", 3)
      'Sbwkrq3.6'
      >>> encrypt_caesar("", 3)
      ''
      """
    o = ""
    for c in plaintext:
        if c.islower():
            o += convert(c, key, 'a')
        elif c.isupper():
            o += convert(c, key, 'A')
        else:
            o += c
    return o

def decrypt_caesar(plaintext, key):
    """
       Decrypts a ciphertext using a Caesar cipher.

       >>> decrypt_caesar("SBWKRQ", 3)
       'PYTHON'
       >>> decrypt_caesar("sbwkrq", 3)
       'python'
       >>> decrypt_caesar("Sbwkrq3.6", 3)
       'Python3.6'
       >>> decrypt_caesar("", 3)
       ''
       """
    return encrypt_caesar(plaintext, -key)

key = 3
plaintext = 'PYTHON.'
e = encrypt_caesar(plaintext, key)
d = decrypt_caesar(e, key)

print(d)
print(e)