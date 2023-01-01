import io

value="good"
encryp=""
decryp=""
class EncrypType:
    ENCRYP = 0
    DECRYP = 1



def Test01(crypto_type):
    global encryp
    global decryp
    for i in range(len(value)):
        if crypto_type == EncrypType.ENCRYP:
            encryp = encryp + chr(ord(value[i])+2) 
        elif crypto_type == EncrypType.DECRYP:
            decryp = decryp + chr(ord(value[i])-2) 
        

def Test02(crypto_type):
    global encryp
    global decryp
    len_val = len(value)
    for i in reversed(range(len_val)):
        if crypto_type == EncrypType.ENCRYP:
            encryp = encryp + value[i]
        elif crypto_type == EncrypType.DECRYP:
            decryp = decryp + value[i] 


#Test01(EncrypType.ENCRYP)
#print("encryp : " , encryp)
#print("decryp : " , decryp)

Test02(EncrypType.ENCRYP)
print("encryp : " , encryp)
print("decryp : " , decryp)
