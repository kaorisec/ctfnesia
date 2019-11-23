import string
import itertools

def adfgvx(val):
        val = val.lower()
        encode = ""
        num = ""
        table = ["8","p","3","d","1","n",
                 "l","t","4","o","a","h",
                 "7","k","b","c","5","z",
                 "j","u","6","w","g","m",
                 "x","s","v","i","r","2",
                 "9","e","y","0","f","q"]
        jumble = "adfgvx"
        for char in val:
            row = table.index(char) // 6
            col = table.index(char) %6
            num += str(row) + str(col)
        for i in range(len(num)):
            tmp = int(num[i])
            encode += jumble[tmp]
        return encode

def column(key,userval):
    try:
        assert key.isalpha()
        key = key.lower()
        userval = userval.lower()
        col=len(key)
        userval=userval.replace(' ','')
        if((len(userval)%col)!=0):
            userval+="x"*(len(userval)%col)

        o=[]
        for i in key:
            o.append(i)

        h=[]
        for i in range(col):
            h.append(userval[i:len(userval):col])

        dic=dict(zip(o,h))
        so=sorted(dic.keys())
        yoay = ''.join(dic[i]for i in so)
        return yoay

    except:
        print("Whoops, Wrong maneh. repeat char a?")

def check(key):
    key = key.lower()
    char = "abcdefghijlkmnopqrstuvwxyz"
    for i in char:
        count = key.count(i)
        if count > 1:
            return false

def encryptA(key,userval,counter=2):
        key = key.lower()
        userval = userval.lower()
        col=len(key)
        userval=userval.replace(' ','')
        if((len(userval)%col)!=0):
            userval+="x"*(len(userval)%col)

        o=[]
        for i in key:
            o.append(i)

        h=[]
        for i in range(col):
            h.append(userval[i:len(userval):col])

        dic=dict(zip(o,h))
        so=sorted(dic.keys())
        yeay = ''.join(dic[i]for i in so)
        return yeay

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk



def prepare_input(dirty):
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
    if len(dirty) < 2:
        return dirty
    for i in range(len(dirty)-1):
        clean += dirty[i]
        if dirty[i] == dirty[i+1]:
            clean += 'X'
    clean += dirty[-1]
    if len(clean) & 1:
        clean += 'X'
    return clean

def generate_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    return table

def encryptC(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
        if row1 == row2:
            ciphertext += table[row1*5+(col1+1)%5]
            ciphertext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[((row1+1)%5)*5+col1]
            ciphertext += table[((row2+1)%5)*5+col2]
        else:
            ciphertext += table[row1*5+col2]
            ciphertext += table[row2*5+col1]
    return ciphertext

def encryptB(plain):
    try:
        assert plain.isalpha()
        plain = plain.lower()
        for char in plain:
            row = int((ord(char) - ord('a')) / 5) + 1
            col = ((ord(char) - ord('a')) % 5) + 1
            if char == 'k':
                row = row - 1
                col = 5 - col + 1
            elif ord(char) >= ord('j'):
                if col == 1 :
                    col = 6
                    row = row - 1
                col = col - 1
            print(row, col, end =' ', sep ='')
        print("")
    except:
        print("Opps, Somethin Went Wrong")


if __name__ == "__main__":
    plain = input("plain: ")
    key = "Hology"
    keyC = "momogi"
    shift = 16
    A = encryptA(key,plain)
    C = encryptC(A,keyC)
    D = ""
    plain = plain.upper()
    print(plain)
    for i in range(len(plain)):
        tmp = ord(plain[i]) + (shift%26)
        if(tmp > 90):
            D += chr((tmp + 65) % 91)
        else:
            D += chr(tmp)
    keyE = "arek"
    E = adfgvx(D)
    E = column(keyE,E)
    encryptB(E)

