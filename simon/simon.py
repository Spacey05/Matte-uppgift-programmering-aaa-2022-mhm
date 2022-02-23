
x = [4,2,7,5,23,16,8,4]
def medelvärde(x):
    avg = sum(x) / len(x)
    return avg

medelvärde = medelvärde(x)

print ("medelvärde av lista =", medelvärde)

def standardavvikelse(x):
    n = len(x)
    medel = sum(x) / n
    var = sum((x- medel)**2 for x in x) / n
    standardavvikelse = var ** 0.5
    return standardavvikelse

print("standardavvikelse av lista =", standardavvikelse(x))

def Variationsbredd(x):
    storlek = len(x)-1
    vb =sorted(x)[storlek] - sorted(x)[0]
    return vb

print ("variationsbredden av lista =",Variationsbredd(x))

def medianen (x):
    storlek = len(x)
    med = storlek // 2
    if storlek % 2:
        return sorted(x)[med]
    return sum(sorted(x)[med - 1:med + 1]) / 2
print ("medianen av lista=", medianen(x))