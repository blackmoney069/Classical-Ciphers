# this is the code for encryption of affine cipher


def encode_affine(m,a,b):
    c = ""
    for i in m:
        asci_value = ord(i)
        #if i is a space we will ignore it
        if(asci_value==32):
            cip_let= asci_value
    
        #IF i is hella small alphabet it lies between 97 and 122
        elif(asci_value>=97 and asci_value<=122):
            asci_value = asci_value-97
            asci_value = a*(asci_value)+b
            asci_value = asci_value%26
            cip_let = asci_value+97
        # for capital alphabets
        elif(asci_value>=65 and asci_value<=90):
            asci_value = asci_value-65
            asci_value = a*(asci_value)+b
            asci_value = asci_value%26
            cip_let = asci_value+65     

        c = c+ chr(cip_let)
    return c

print("please select Encode(1) or decode(0)") #allows to run both encoding and decoding 
i = int(input())

if(i==1): # encoding
    print("Please enter the plaintext")
    m = str(input())
    import random
    a = random.randint(1,26)
    b = random.randint(1,26)
    c = encode_affine(m,a,b)
    print("the ciphertext is ", c, "and the key is (",a,",",b ,").")

def decode_affine(c): #this will decode the cipher
    for a in range(1,27):
        for b in range(1,27): #select keys starting from 1 to 26
            m = ""
            for i in c:
                asci_val = ord(i)
                if(asci_val==32):
                    dec_val = i
                
                elif(asci_val>=97 and asci_val<=122):
                    asci_val = asci_val-97
                    dec_val = ((asci_val-b)/a)%26
                    dec_val = dec_val +97
                
                elif(asci_val>=65 and asci_val<=90):
                    asci_val = asci_val-65
                    dec_val = ((asci_val-b)//a)%26
                    print(dec_val)
                    dec_val = dec_val +65  
                m = m+chr(dec_val)
            
            print(m,"\n")

if(i==0):
    print("please enter the ciphertext")
    c = str(input())
    decode_affine(c)
    print("select the meaningful sentence")

