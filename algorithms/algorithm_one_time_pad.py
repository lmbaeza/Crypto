
import random

def random_char(from_value, to_value):
    char_from = ord(from_value)
    char_to = ord(to_value)
    return chr(random.randrange(char_from, char_to+1))

def int_bin(number):
    ans = ""
    while number > 0:
        ans += str(number % 2)
        number //= 2
    ans = ans[::-1]
    prefix = "0"*(8-len(ans))
    return prefix + ans

def bin_int(binary):
    ans = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i]=='1': ans |= int(1 << i)
    return ans

class OneTimePad:
    
    def encrypt(self, txt, key):
        txt_bin = ""
        key_bin = ""
        
        for i in range(len(txt)):
            txt_bin += int_bin(ord(txt[i]) - ord('A'))
            
        for i in range(len(key)):
            key_bin += int_bin(ord(key[i]) - ord('A'))
        
        ans = ""
        for i in range(len(txt_bin)):
            ans += str(int(txt_bin[i]) ^ int(key_bin[i]))
        letters = []
        letter = ""
        for i in range(len(ans)):
            letter += ans[i]
            if (i+1) % 8 == 0:
                letters.append(letter)
                letter = ""
        output = ""
        for bin_chr in letters:
            output += chr(bin_int(bin_chr) + ord('A'))
        return output
    
    def decrypt(self, encry, key):
        txt_bin = ""
        key_bin = ""
        
        for i in range(len(encry)):
            txt_bin += int_bin(ord(encry[i]) - ord('A'))
            
        for i in range(len(key)):
            key_bin += int_bin(ord(key[i]) - ord('A'))
        
        ans = ""
        for i in range(len(txt_bin)):
            ans += str( ( int(txt_bin[i]) ^ int(key_bin[i]) )  )
        
        letters = []
        letter = ""
        for i in range(len(ans)):
            letter += ans[i]
            if (i+1) % 8 == 0:
                letters.append(letter)
                letter = ""
                
        output = ""
        for bin_chr in letters:
            output += chr(bin_int(bin_chr) + ord('A'))
        return output


message = input()
message = message.replace(" ", "")
message = message.upper()

key = ""
for i in range(len(message)):
    key += random_char('A', 'Z')

cipher = OneTimePad()

encrypt = cipher.encrypt(message, key)
print("Encrypt:", encrypt)
decrypt = cipher.decrypt(encrypt, key)
print("Decrypt:", decrypt)
