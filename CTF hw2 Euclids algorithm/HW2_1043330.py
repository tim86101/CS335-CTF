import pwn
def Euclidean(x,y):
    la=1
    lb=0
    ra=0
    rb=1
    gcd=1
    
    while x>0 and y>0 :
        adiv = int(x/y)
        x = x % y
        la = la - ra * adiv
        lb = lb - rb * adiv
    
        if x==0:
            gcd=y
            if ra<0:
                ra+=10000
            if rb<0:
                rb+=10000
            result=str(gcd)+","+str(ra)+","+str(rb)
            print("answer ",result)
            conn.sendline(result)
            break

        bdiv = int(y/x)
        y = y % x
        ra = ra - la * bdiv
        rb = rb - lb * bdiv

        if y==0:
            gcd=x
            if la<0:
                la+=10000
            if lb<0:
                lb+=10000
            result=str(gcd)+","+str(la)+","+str(lb)
            print("answer ",result)
            conn.sendline(result)
            break
        


conn =pwn.process(["nc","140.138.77.30","6015"])
for i in range(0,5):
    conn.recvline()
for i in range(0,1000):

    newline = conn.recvline()
    print(newline)
    
    newline = str(newline)
    newline = newline.replace( "b" , "" )
    newline = newline.replace( "'" , "" )
    newline = newline.replace( "x" , "" )
    newline = newline.replace( "i" , "" )
    newline = newline.replace( "s" , "")
    newline = newline.replace( "\\", "")
    newline = newline.replace( "y" , "")
    newline = newline.replace( "," , "")
    newline = newline.replace( "n" , "")
    
    newstr = newline.split(" ")
    xnum=int(newstr[2])
    ynum=int(newstr[5])
    
    Euclidean(xnum,ynum)
    
    
    
    


flag = conn.recvline()
print (flag)

