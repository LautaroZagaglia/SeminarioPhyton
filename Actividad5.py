from turtle import ondrag


texto="""Yo estaba en onda, pero luego cambiaron la onda. 
Ahora la onda que traigo no es onda, y la onda de onda me parece muy mala onda. 
¡Y te va a pasar a ti!"""

palabras = texto.lower().split()
pal= input("ingresar palabra")
cont=0
for palabra in palabras:
    if pal in palabra:
        cont=cont+1
print("palabra buscada: ",pal," y se an encontrado: ",cont)
