
print('Please enter the size of the S-array')
S_len = int(input())
S_array = [0]*S_len
T_array = [0]*S_len

for i in range(0,S_len):
    S_array[i] = i

print("please enter the size of the key")
key_len = int(input())

print("please enter the key")
key_str = str(input())

K_array = [0]*key_len
for i in range(0,key_len):
    K_array[i] = int(key_str[i])

for i in range(0,S_len):
    T_array[i] = int(key_str[i%key_len])

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
        j = (j+S[i]+K[i])%S_len
        swap_array(S,i,j)
        print_array(S)


key_scheduling_RC4(S_array,T_array)

def stream_generation(S,key_size):
    i,j =0
    outkey =[]
    gen_size=0
    while(gen_size <key_size):
        i = (i+1)%S_len
        j = (j+S[i])%S_len
        swap_array(S,i,j)
        t = (S[i]+S[j])%S_len
        outkey.append(S[t])
        gen_size+=1;
    return outkey



    


