#Simple substitution Cipher
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def substitutionMakeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def substitutionEncrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def substitutionDecrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(),c) for c in cipher)

ptext = input("Enter plain text: ")
ptext.replace(' ','')

subkey = substitutionMakeKey(alphabet)
print("Key for substitution Cipher ",subkey)
cipher2 = substitutionEncrypt(ptext, subkey, alphabet)
print("Encryption substitution cipher): ",cipher2)

print()

dec1 = substitutionDecrypt(cipher2, subkey, alphabet)
print("Decryption Substitution Cipher: ",dec1)

