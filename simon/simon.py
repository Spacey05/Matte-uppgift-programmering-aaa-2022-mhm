

def medelvärde(x):
    avg = sum(x) / len(x)
    return avg

#---------------------------------------------------------------

def standardavvikelse(x):
    n = len(x)
    medel = sum(x) / n
    var = sum((x- medel)**2 for x in x) / n
    standardavvikelse = var ** 0.5
    return standardavvikelse

#--------------------------------------------------------------

def Variationsbredd(x):
    storlek = len(x)-1
    vb =sorted(x)[storlek] - sorted(x)[0]
    return vb

#--------------------------------------------------------

def medianen (x):
    storlek = len(x)
    med = storlek // 2
    if storlek % 2:
        return sorted(x)[med]
    return sum(sorted(x)[med - 1:med + 1]) / 2


#-------------------------------------------------------------

def kvartilun(x):
    x.sort()

    return x

#---------------------------------------------------------------

def kvartilup(x):
    x.sort()
    return x

#---------------------------------------------------------------

def kvartilavstånd(x):
    return 

#---------------------------------------------------------------

def residualerna(y):
    w = y
    for n in range(len(w)):
        w[n][1] = w[n][1] - (k+m)
    return w


x = [1,2,3,4,5,6,7,8]

y = [[5,3],[9,4],[3,2],[5,6]]

k = 4
m = 3

print ("medelvärde av lista =", medelvärde(x))

print("standardavvikelse av lista =", standardavvikelse(x))

print ("variationsbredden av lista =",Variationsbredd(x))

print("Medianen av listan=", medianen(x))

print("undre kvartilen=",medianen(kvartilun(x)))

print ("övrekvartilen=",medianen(kvartilup(x)))

print("kvartilavsståndet=", kvartilavstånd(x))

print("residualerna=", residualerna(y))