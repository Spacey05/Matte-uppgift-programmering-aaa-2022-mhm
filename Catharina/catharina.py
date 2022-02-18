
#Medelvärdet av tal i given lista 
def medelvärde(x):
    avg = sum (x) / len (x)
    return avg
lista = [1,2,3,4,5]
medelvärde = medelvärde(lista)

print ("medelvärde av lista är", medelvärde)

#variationsbredd av tal i given lista
lista = [1,2,2,4,6,6,9]

st=len(lista)-1
vb=lista[st] - lista[0]
print("Variationsbredden är", (vb))

#



 


