
def square_and_multiply(m, e, n):
    # Überprüfen der Authentizität der Signatur durch
    # Square and Multiply, wie in den Folien erwähnt, 
    # zb. 920 (Nachricht), 157 (e), 2773 (n) ergibt den 
    # dekodierten Text 192, 192 kann ich mit dieser Funktion
    # schneller berechnen, sonst müsste ich m hoch e rechnen,
    # was bei PCs z.T. nicht mehr darstellbar wäre...
    print("Berechung von: "+ str(m) + "hoch" + str(e) + " mod " + str(n))
    # Initialisiere eine Liste mit den Werten 0 und 1.
    # m param: Nachricht die verschlüsselt wird
    # e param:Teilerfremde Zahl zu phi
    # n param: Produkt der zwei Primzahlen
    values = [0, m% n]
    e_original = e

    # Wandle das Exponenten-Bitmuster in eine Liste von Exponenten um.
    exponents = []
    while e > 0:
        exponents.append(e % 2)
        
        e //= 2
        
    exponents.reverse()
    print("Die Binäre Darstellung von " + str(e_original)+" ist: "+ str(exponents))

    # Berechne die Werte der Potenzen von b modulo m.
    for exponent in exponents[1:]:
        # Quadriere den letzten Wert in der Liste und moduliere ihn.
        values.append((values[-1] ** 2) % n)
        # Wenn der aktuelle Exponent 1 ist, multipliziere den letzten Wert
        # mit b und moduliere ihn.
        if exponent == 1:
            values[-1] = (values[-1] * values[1]) % n
        print("Zwischenresultate: " + str(values[-1]))

    # Gib den letzten Wert in der Liste zurück.
    return values[-1]

# Test der Funktion wie beim Beispiel in der Übung auf den Folien:
print(square_and_multiply(920, 17, 2773)) 

