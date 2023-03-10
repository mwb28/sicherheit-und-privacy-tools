def ext_euclid(e, f):
    x1 = 1
    x2 = 0
    x3 = f
    y1 = 0
    y2 = 1
    y3 = e
    print(" q  x1 x2 x3 y1 y2 y3  t1  t2  t3")
    while (y3 > 0):
        if y3==0:
              return print (x3 + "ist keine Inverse")
        if y3 == 1:
            return print(str(y3)+ " ist ggT, "+ str(y2)+" ist inverse")
        else:
            printlist = []
            q = x3//y3
            t1 = x1-q*y1
            t2 = x2-q*y2
            t3 = x3-q*y3
            printlist.extend([q,x1,x2,x3,y1,y2,y3,t1,t2, t3])
            print(printlist)
            x1 = y1
            x2 = y2
            x3 = y3
            y1= t1
            y2 = t2
            y3 = t3


def primfaktoren(n):

    """ zerlegt eine Zahl in ihre Primfaktoren

    >>> primfaktoren(24)
    [2, 2, 2, 3]

    """

    faktoren = []
    z = n
    while z > 1:
        # bestimme den kleinsten Primfaktor p von z
        i = 2
        gefunden = False
        while i*i <= n and not gefunden:
            if z % i == 0:
                gefunden = True
                p = i
            else:
                i = i + 1
        if not gefunden:
            p = z
        # füge p in die Liste der Faktoren ein
        faktoren = faktoren + [p]
        z = z // p
    return faktoren




def ext_euclid_ohneprint(e, f):
    x1 = 1
    x2 = 0
    x3 = f
    y1 = 0
    y2 = 1
    y3 = e
    while (y3 > 0):
        if y3==0:
              return  x3 
        if y3 == 1:
            return y2
        else:
            q = x3//y3
            t1 = x1-q*y1
            t2 = x2-q*y2
            t3 = x3-q*y3
       
            x1 = y1
            x2 = y2
            x3 = y3
            y1= t1
            y2 = t2
            y3 = t3

def schluessel_berechnen(verschl_Zahl, e, n):
    print("verschlüsselte Zahl= " + str(verschl_Zahl))
    print("öffentlicher Schlüssel= " + str(e))
    print("Produkt der Primfaktoren(p*q)= " + str(n))
    primfaktoren_list = primfaktoren(n)
    print("primfaktoren = "+str(primfaktoren_list))
    phi = (primfaktoren_list[0]-1) * (primfaktoren_list[1]-1)
    print ("phi=" +str(phi) + " (p-1)(q-1)")
    print(str(e)+ "*d mod phi(" +str(n)+") = 1")
    print(str(e)+ "*d mod"+ str(phi) +"= 1")
    print("inverse berechnen:")
    ext_euclid(e,phi)
    d = ext_euclid_ohneprint(e,phi)
    if d <0:
        print (str (d) +"mod phi als d berechnen:")
        d = d % phi
        print("d= " + str(d))
    print ("Öffentlicher Schlüssel (e, n): " +str(e) + ", " + str(n))
    print ("privater Schlüssel(d,n): " +str(d) + ", " + str(n))
    print ("verschlüsselte_Zahl^d mod n = " +str(verschl_Zahl)+ "^"+str(d)+ "mod"+ str(n))

    print ("Ursprüngliche Zahl entschlüsselt: ="+ str((verschl_Zahl**d)%n))


schluessel_berechnen(920,157,2773)

