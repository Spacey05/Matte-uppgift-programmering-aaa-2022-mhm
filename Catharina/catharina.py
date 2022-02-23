x = [4,2,7,5,23,16,8,4]

#Medelvärdet av tal i given lista 
def medelvärde (x):
    avg = sum(x) / len(x)
    return avg

medelvärde = medelvärde(x)

print ("medelvärde av lista är", medelvärde)

#Standardavvikelse av tal i given lista
def standardavvikelse (x):
    n = len(x)
    medel = sum(x) / n
    var = sum((x- medel)**2 for x in x) / n
    standardavvikelse = var ** 0.5
    return standardavvikelse

print("standardavvikelse av lista =", standardavvikelse(x))

#Variationsbredd av tal i given lista
def variationsbredd (x):
    storlek = len(x)-1
    vb = sorted(x)[storlek] - sorted(x)[0]
    return vb

print("Variationsbredden är", variationsbredd(x))

#Median av tal i given lista
def median (x):
    storlek = len(x)
    med = storlek // 2
    if storlek % 2:
        return sorted(x)[med]
    return sum(sorted(x)[med - 1:med + 1]) / 2

print ("medianen av listan=", median(x))

#Kvartilerna i given lista
def kvartilun(x):
    x.sort()
    return x[0:int(len(x)/2)]

print ("undre kvartilen =", median(kvartilun(x)))

def kvartilup (x):
    x.sort()
    return x[int(median(x)):-1]

print ("övre kvartilen =", median(kvartilup(x)))
    
def kvartilavstånd (x):
    up = median(kvartilup(x))
    un = median(kvartilun(x))
    return up - un

print ("kvartilavstånd =", kvartilavstånd(x))
 


