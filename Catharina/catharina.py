x = [4,2,7,5,23,16,8,4]

#Medelvärdet av tal i given lista 
def medelvärde (x):
    avg = sum(x) / len(x)
    return avg

medelvärde = medelvärde(x)

#Standardavvikelse av tal i given lista
def standardavvikelse (x):
    n = len(x)
    medel = sum(x) / n
    var = sum((x- medel)**2 for x in x) / n
    standardavvikelse = var ** 0.5
    return standardavvikelse

#Variationsbredd av tal i given lista
def variationsbredd (x):
    storlek = len(x)-1
    vb = sorted(x)[storlek] - sorted(x)[0]
    return vb

#Median av tal i given lista
def median (x):
    storlek = len(x)
    med = storlek // 2
    if storlek % 2:
        return sorted(x)[med]
    return sum(sorted(x)[med - 1:med + 1]) / 2

#Kvartilerna i given lista
def kvartiler(x):
    x.sort()
    medianen = median(x)
    x1 = []
    x2 = []
    c=0
    for i in x:
        if x[c]< medianen:
            x1.append(x[c])
        elif x[c]> medianen:
            x2.append(x[c])
        c=c+1
    
    print("undrekvartil=", median(x1),"övrekvartilen=",median(x2))
    print("kvartilavstånd",median(x2)-median(x1))



#print för alla def
print ("medelvärde av lista =", medelvärde)
print("standardavvikelse av lista =", standardavvikelse(x))
print("Variationsbredden =", variationsbredd(x))
print ("medianen av listan =", median(x))
kvartiler(x)


