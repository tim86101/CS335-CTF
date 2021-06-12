# coding: latin1
with open("MTPciphertext.txt","r",encoding='utf-8') as file:
    substring=[]
    ciphertext=[]
    while True:
        inputarray = file.read(16)
        if not inputarray:
            break
        for inputnum in inputarray:
            substring.append(ord(inputnum))
        print(substring)
        ciphertext.append(substring)
        substring = []
        if not inputarray:
            break
pos_kyspace = []
keyspace = []
message_space = [32,33,34,39,40,41,44,45,46,48,49,50,51,52,53,54,55,56,57,58,59,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125]
for index in range (0,16):
    for message in message_space:
        pos_kyspace.append(ciphertext[0][index] ^ message)
 #   print(message_space)
    for i in range (1,len(ciphertext)):
        for key in pos_kyspace:
            newmessage = (ciphertext[i][index] ^ key)
            if newmessage not in message_space:
                pos_kyspace.remove(key);
    print(pos_kyspace)
    keyspace.append(pos_kyspace[0])
    pos_kyspace=[]
print(keyspace)
origin=""
for i in range (1,len(ciphertext)):
    for index in range (0,16):
        origin+=str(chr(ciphertext[i][index] ^ keyspace[index]))
    print (origin)
    origin=""
