
print('Please enter the size for the arrays')
cip_len = int(input())
S_array = [0]*cip_len
K_array = [0]*cip_len

for i in range(0,cip_len):
    S_array[i] = i

print("please enter the siez of the key")
key_len = int(input())

print("please enter the key")
key_str = str(input())

for i in range(0,cip_len):
    K_array[i] = int(x[i%key_len])

def swap_array(S, i,j):
    c = S[i]
    S[i] = S[j]
    S[j] = c

def print_array(S_array):
    for i in S_array:
        print(i,end="")
    print("\n")

def key_scheduling_RC4(S,K):
    j=0
    for i in range(0,8):
        j = (j+S[i]+K[i])%8
        swap_array(S,i,j)
        print_array(S)


key_scheduling_RC4(S_array,K_array)



