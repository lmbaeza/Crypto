class Rot13:
    
    def __init__(self):
        self.ALPHA = 26
        
    def encrypt(self, txt):
        key = 13
        txt = txt.replace(" ", "")
        txt = txt.upper()
        output = ""
        n = len(txt)
        for i in range(n):
            output += chr( ((ord(txt[i])-ord('A'))+key)%self.ALPHA + ord('A'))
        return output
    
    def decrypt(self, encry):
        key = 13
        output = ""
        n = len(encry)
        for i in range(n):
            output += chr( (((ord(encry[i])-ord('A'))-key)+self.ALPHA)%self.ALPHA + ord('A'))
        return output
    

message = "SOME MESSAGE"

cesar = Rot13()
encrypt = cesar.encrypt(message)

print("Encrypt:", encrypt)

decrypt = cesar.decrypt(encrypt)
print("Decrypt:", decrypt)
