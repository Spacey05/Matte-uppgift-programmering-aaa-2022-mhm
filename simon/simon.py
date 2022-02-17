
def medelvärde(x):
    avg = sum(x) / len(x)
    return avg
lista = [1,7,2,4,3,1]
medelvärde = medelvärde(lista)

print ("medelvärde av lista", medelvärde)

def standardavvikelse(x):
    n = len(x)
    medel = sum(x) / n
    var = sum((x- medel)**2 for x in x) / n
    standardavvikelse = var ** 0.5
    return standardavvikelse


x = [10,11,12,13,14,15,16,17,18,19,20]

print("standardavvikelse av lista", standardavvikelse(x))