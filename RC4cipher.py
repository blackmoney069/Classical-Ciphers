
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
        print(i,end=" ")
    print("\n")

def key_scheduling_RC4(S,K):
    j=0
    for i in range(0,8):
        j = (j+S[i]+K[i])%S_len
        swap_array(S,i,j)
        print_array(S)


# key_scheduling_RC4(S_array,T_array)

def stream_generation(S,key_size):
    S_len = len(S)
    j =0
    i=0
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

print("please enter the size of the key required")
req_key_size = int(input())
# S = [31,26,7,10,23,3,20,30,14,4,16,15,29,8,2,9,21,19,11,6,12,17,25,24,0,22,13,27,5,1,28,18]
outkey = stream_generation(S_array,req_key_size)

print_array(outkey)

# TEST RUN 1
# S-SIZE = 256 , key = 35017642 final S array = 3911122334445381102013141516171819202122424252627282930313233535363738394041424364546474849505152754555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169170171172173174175176177178179180181182183184185186187188189190191192193194195196197198199200201202203204205206207208209210211212213214215216217218219220221222223224225226227228229230231232233234235236237238239240241242243244245246247248249250251252253254255

    


