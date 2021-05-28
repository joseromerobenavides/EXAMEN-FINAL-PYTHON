texto=input ("tu texto:  ")

if texto==texto.upper(): 
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc="abcdefghijklmnñopqrstuvwxyz"
k=int (input ("Valor de desplazamiento: "))

cifrado=""
for c in texto:
    if c in abc:
        cifrado += abc[(abc.index(c)+k%(len(abc)))]
    else:
        cifrado+=c 
print("texto cifrado: ",cifrado)