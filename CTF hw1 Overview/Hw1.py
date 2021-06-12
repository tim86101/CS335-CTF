import pwn

conn =pwn.process(["nc","140.138.77.30","6007"])
for i in range(0,1000):
    print(i)

    newline = conn.recvline()
    print(newline)
    newline = conn.recvline()
    print(newline)
    newline = str(newline)
    newline = newline.replace( "b" , "" )
    newline = newline.replace( "'" , "" )
    newline = newline.replace( "[" , "" )
    newline = newline.replace( "," , "" )
    newline = newline.replace( "n" , "")
    newline = newline.replace( "\\", "")
    newline = newline.replace( "]" , "")

    newstr = newline.split(" ")
    newstr = list(map(int , newstr))
    newstr.sort()


    newstr = list(map(str , newstr))
    sortedarr=newstr[0]
    for j in range(1,10):
        sortedarr = sortedarr + "," + newstr[j]
    print(sortedarr)
    
    
  #  useless = conn.recvline()
  #  print(useless)

    conn.sendline(sortedarr)
flag = conn.recvline()
print (flag)
