def encrypt(text,key):
	result=""
	for i in range(len(text)):
		char = text[i]
		if char==" ":
			result+=" "
			continue
		if char.isupper():
			result+=chr((ord(char)+key-65)%26 +65)
		else:
			result+=chr((ord(char)+key-97)%26 +97)
	return result

def decrypt(ciphertext,key):
	result=""
	for i in range(len(ciphertext)):
		char = ciphertext[i]
		if char==" ":
			result+=" "
			continue
		if char.isupper():
			result+=chr((ord(char)-key-65)%26+ 65)
		else:
			result+=chr((ord(char)-key-97)%26+ 97)
	return result
			

text = "defend the east wall of the castle"

key = 1

print("Plain Text:",text)
print("Key:",key)
ciphertext = encrypt(text,key)
print("Cipher Text:",ciphertext)
print("Decrypted text:",decrypt(ciphertext,key))
