import io

value="good"
encryp=""
decryp=""


def Test01(crypto_type):
    global encryp
    global decryp
    if crypto_type == 0:
        for i in range(len(value)):
            encryp = encryp + chr(ord(value[i])+2) 
    else:
        for i in range(len(value)):
            decryp = decryp + chr(ord(value[i])-2) 
        

#Test01(1)
#print("encryp : " , encryp)
#print("decryp : " , decryp)
