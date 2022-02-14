# this is the code for encryption of affine cipher

print("please enter the plaintext")
m = str(input())

import random
a = random.randint(1,26)
b = random.randint(1,26)
#these are the keys that we will be using for the encryption

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

    elif(asci_value>=65 and asci_value<=90):
        asci_value = asci_value-65
        asci_value = a*(asci_value)+b
        asci_value = asci_value%26
        cip_let = asci_value+65     

    c = c+ chr(cip_let)

print("the ciphertext is ", c, "and the key is (",a,",",b ,").")
