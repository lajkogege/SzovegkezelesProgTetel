
#1.	Számoljuk meg hány szóköz van a szövegben!
def elso(szoveg:str):
    print("1.feladat:")
    i:int=0
    szokoz:int=0
    while i<len(szoveg):
        if szoveg[i] == " ":
            szokoz+=1
        i+=1
    print(f"Ennyi szóköz van a mondatban:{szokoz}")
    return szokoz

#2.	Írjuk ki a szöveget a képernyőre szóközök nélkül. A továbbiakban ezzel a szöveggel dolgozzunk!
def masodik(szoveg:str):
    print("2.feladat:")
    i:int=0
    osszeg:str=""
    while i<len(szoveg):
        if szoveg[i] != " ":
           osszeg += szoveg[i]
        i+=1
    print(szoveg)
    return szoveg

def harmadik(szoveg:str):
    print("3.feladat a:")
    kisbetus_szoveg:str= szoveg.casefold()
    print(kisbetus_szoveg)
    print("3.feladat b:")
    szoveg=szoveg.replace("á", "a")
    szoveg = szoveg.replace("é", "e")
    szoveg = szoveg.replace("í", "i")
    szoveg = szoveg.replace("ó", "o")
    szoveg = szoveg.replace("ő", "ö")
    szoveg = szoveg.replace("ű", "ü")
    szoveg = szoveg.replace("ú", "u")
    print(szoveg)
    print("3.feladat c:")
    i=len(szoveg)-1
    while i>=0:
        i-=1
        print(szoveg[i], end=" ")
    return szoveg

#def negyedik(szoveg):
    #i:int=0
    #while i<len(szoveg):
        #if szoveg[i]=="a"







