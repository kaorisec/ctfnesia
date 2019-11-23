print 'KKSI 2019 REGIONAL SUROBOYO'
print '==========================='
 
def scramble(x):
    return [ chr(i) for i in x ]
 
def flippity(x):
    return ''.join([ ''.join(i) for i in zip(x[1::2], x[0::2]) ])
 
def go():
    password = raw_input('Password: ')
    if len(password) != 22:
        return False
    if ord(password[11]) != 101 or ord(password[5]) != 50 or ord(password[16]) != 112 or ord(password[12]) != 100 or ord(password[18]) != 115 or ord(password[21]) != 33 or ord(password[13]) != 97 or ord(password[9]) != 95 or ord(password[14]) != 110 or ord(password[17]) != 97 or ord(password[7]) != 49 or ord(password[1]) != 107 or ord(password[15]) != 95 or ord(password[19]) != 115 or ord(password[20]) != 33 or ord(password[3]) != 105 or ord(password[10]) != 109 or ord(password[8]) != 57 or ord(password[6]) != 48 or ord(password[2]) != 115 or ord(password[4]) != 95 or ord(password[0]) != 107:
        return False
    return flippity(scramble([117, 115, 115, 107, 115, 101]))
 
print go()
