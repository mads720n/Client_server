"""
I bunden af pyCharm står der "Python Packages"
klik der og indtast matplotlib.
Herefter skal i trykke på knappen "Install" for at installere og anvende
pakken i pyCharm IDE'et
"""
#Nuværende problem, 1: at tegne skibene, 2: få et bedre display vindue :)




import matplotlib.pyplot as plt

#Grid plot configuration
w = 3
h = 3
d = 70

global xBeskudt
global yBeskudt
xBeskudt = []
yBeskudt = []

xBådKoordinater = [3,4,5]
yBådKoordinater = [2,2,0]
print("Nu skal du til at indtaste x og y koordinater i spillet\n*******  SÆNK SLAGSKIBE  *******\n\n")

"""
Her skal du selv tilrette koden i def plotSkudkoordinat(skud)
så du får de aktuelle skudkordinater plottet ud
"""
def plotSkudkoordinat(x,y):
    plt.ion()
    plt.figure(figsize=(w, h), dpi=d)
    plt.axis([0, 5, 0, 5])
    plt.axis('image')
#    x = [1, 2, 4]
#    y = [1, 3, 3]
    size = 500
    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.scatter([x], [y])
#    plt.savefig("out.png")
    plt.show()
    plt.pause(1)
    plt.close()

def hitCheck(x,y):
    if x in xBådKoordinater:
        n = xBådKoordinater.index(x)
        yTjek = yBådKoordinater[n]
#yTjek eksitere fordi man ikke kan hente index i en if sætning :), det var sjovt.
        if yTjek == y:
            print("hit","\n")
            xBådKoordinater.pop(n)
            yBådKoordinater.pop(n)
    else:
        print("miss","\n")

count = 0
while count < 5:
    count = count + 1

    print("Skud nummer: ",(count+1),"Antal skud tilbage", 5-(count-1))
    xKoordinat = int(input("Indtast x koordinat "))
    yKoordinat = int(input("Indtast y koordinat "))
    skudKoordinater = [xKoordinat, yKoordinat]

    if 1 <= int(xKoordinat) <= 10 and 1 <= int(yKoordinat) <= 10:
     print("valide skudkoordinater er: ", skudKoordinater,"\n")

     if xKoordinat in xBeskudt and yKoordinat in yBeskudt:
        print("[DUPLICATE SHOT aka DUM DUM]", "\n")
        count = count - 1
     else:
        xBeskudt.append(xKoordinat)
        yBeskudt.append(yKoordinat)

        plotSkudkoordinat(xBeskudt,yBeskudt)

        hitCheck(xKoordinat, yKoordinat)
    else:
            print("invalide skudkoordinater prøv igen: ", skudKoordinater,"\n")
