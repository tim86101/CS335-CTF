import pwn
import base64

def sendRequest(iv,cipher):
    request = str(iv) + ",b'" +str(cipher[0])+"'"
    #print(request)
    #request = request.replace("][","] , b'")
    print(request)
    conn.sendline(request)



conn =pwn.process(["nc","140.138.77.30","6016"])
newline = conn.recvline()
print (newline)


newline =str(newline[18:])
newline = newline.replace('b"',"")
newline = newline.replace('"',"")
newline = newline.replace("[","")
newline = newline.replace("] ","")
newline = newline.replace("b'","")
newline = newline.replace("'\\n","")
newstr = newline.split(", ")
IV = newstr[0:16]
ciphertext = newstr[16:]

print(type(IV))

IV = list(map(int,IV))
newIV = IV.copy()
paddingnum = 0;
print("IV = ",IV)
print("newIV = ",newIV)
for index in range (0,len(newIV)):
    print("IV1 = ",IV)
    newIV[index] = 0
    #print(newIV[index])
    #print("newIV = ",newIV)
    #print("IV = ",IV)
    #print("newIV = ",newIV)
    sendRequest(newIV,ciphertext)
    result = str(conn.recvline())
    print (result)
    if result == ("b'RightPadding\\n'"):
        paddingnum += 1
    else:
        print(paddingnum)
        break;

print("newIV = ",newIV)
print("IV = ",IV)
newIV = IV.copy()

for index in range (0,14):
    newIV[index] = 0

print("newIV = ",newIV)
print("IV = ",IV)
sendRequest(newIV,ciphertext)
result = str(conn.recvline())
print (result)

paddingnum = 16 - paddingnum

message = [0]*16
cinverse = [0]*16
for time in range (15-paddingnum ,-1 ,-1 ):
    for index in range (15,15 - paddingnum , -1 ):
        cinverse[index] = paddingnum ^ newIV[index]

    print ("newIV = ",newIV)
    print ("cinverse = ",cinverse)
    print ("message = ",message)
    
    paddingnum = paddingnum + 1
    
    print ("paddingnum = ",paddingnum)
    for index in range (15,15-paddingnum , -1):
        newIV[index] = newIV[index] ^ (paddingnum-1) ^ paddingnum
    
    
    print ("newIV = ",newIV)
    print ("cinverse = ",cinverse)
    print ("message = ",message)
    for guess in range (0,256):
        newIV[16-paddingnum] = guess
        print("newIV = ",newIV)
        sendRequest(newIV,ciphertext)
        result = str(conn.recvline())
        print (result)
        
        if result == ("b'RightPadding\\n'"):
            break;

print ("cinverse = ",cinverse)
for index in range (15,15 - paddingnum , -1 ):
    cinverse[index] = paddingnum ^ newIV[index]

print ("cinverse = ",cinverse)

for index in range (0,16):
    message[index] = cinverse[index] ^ IV[index]
flag=""
print (message)
for index in range (0,16):
    
    message[index] = chr(message[index])
    print(message[index])
    flag += message[index]
print (flag)
