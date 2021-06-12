import random
#n=3337
n = 995225678611
e = 65537

c = 982661879379

def f(x,alpha):
    return (pow(x,2)+alpha)%n
def pollard(alpha):
    a = 2
    b = 2
    twice = False
    i=0
    while not twice:
       a = f(a,alpha)
       b = f(f(b,alpha),alpha)
       p = gcd(abs(b-a),n )
       """
       print ("a = ",a)
       print ("b = ",b)
       print ("p = ",p)
       print ()
       """
       i=i+1
       if( p > 1 ):
           print(" i =",i)
           return (True , p)
    return ( False , 0 )

def gcd (m,n):
    return m if n==0 else gcd(n,m%n)

def egcd(a,b):
    if a == 0:
        return ( b , 0 , 1 )
    else:
        g,y,x = egcd( b % a , a)
        return ( g, x-( b // a ) * y ,y )

def modinv(a, m):
    g,x,y = egcd ( a , m )
    if g != 1:
        print(" no inverse")
    else:
        return x % m



rand_alpha = random.randint(2,n)
print ("randal",rand_alpha)
print (" N = ",n)
found ,p = pollard(rand_alpha)
while not found:
    rand_alpha = random.randint(2,100)
    found ,p = pollard(rand_alpha)
    if not found:
        print(" fail. ")
print ("p = ",p)
q = n/p
print ("q = ",q)
euler = (p-1)*(q-1)
d = int(modinv( e , euler))
print("d = ",d)

message = pow (c , d , n)
print("message = " , message )

