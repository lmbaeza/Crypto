class Cesar:
    
    def __init__(self):
        self.ALPHA = 26
        
    def encrypt(self, txt, key):
        key = key % self.ALPHA
        txt = txt.replace(" ", "")
        txt = txt.upper()
        output = ""
        n = len(txt)
        for i in range(n):
            output += chr( ((ord(txt[i])-ord('A'))+key)%self.ALPHA + ord('A'))
        return output
    
    def decrypt(self, encry, key):
        key = key % self.ALPHA
        output = ""
        n = len(encry)
        for i in range(n):
            output += chr( (((ord(encry[i])-ord('A'))-key)+self.ALPHA)%self.ALPHA + ord('A'))
        return output
    

message = "SOME MESSAGE"
key = 13

cesar = Cesar()
encrypt = cesar.encrypt(message, key)

print("Encrypt:", encrypt)

decrypt = cesar.decrypt(encrypt, key)
print("Decrypt:", decrypt)
