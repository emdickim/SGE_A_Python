#Igual que la nota que em mereixo(xd, broma)
nota = 10

if 0 <= nota <= 4.99:
    cualificacio = "Suspès"
elif  5 <= nota <= 6.5:
    cualificacio = "Aprovat"
elif 6.5 <= nota <= 8:
    cualificacio = "Notable"
else:
    cualificacio = "Excel·lent"

print(cualificacio)