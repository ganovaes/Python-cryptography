xor= lambda a,b:(a or b) and (int(not(a and b)))

def add(ll):
    key='0000011'
    mm=''
    for j,k in zip(ll,key):
        mm+=str(xor(int(j),int(k)))
    return(chr(int(eval(f'0b{mm}'))))

def  encrypt(msg):
    ms=''
    for i in msg:
        n=str(bin(ord(i)))[2:]
        ms+=add(n)
    print(ms)

while 1:
    encrypt(input('.......'))