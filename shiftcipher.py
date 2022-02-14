#this is the code for shift cipher

print("please enter the plaintext")
m = str(input())

import random
#k = random.randint(1,26)
k = 18
# this will act as our key

c = ""
# this is our cipher text we will traverse through the string and create our final cipher text

for i in m:
    asci_value = ord(i)
    #if i is a space we will ignore it
    if(asci_value==32):
        cip_let= asci_value
    
    #IF i is a small alphabet it lies between 97 and 122
    elif(asci_value>=97 and asci_value<=122):
        asci_value = asci_value-97
        cip_let = asci_value+k
        cip_let = cip_let%26
        cip_let = cip_let+97
   
    #if i is a capital letter it lies between 65 and 90
    elif(asci_value>=65 and asci_value<=90):
        asci_value = asci_value-65
        cip_let = asci_value+k
        cip_let = cip_let%26
        cip_let = cip_let+65

    c = c+chr(cip_let)

print("the cipher text is", c, "and the key is", k)





