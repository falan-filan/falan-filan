import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("şifrenizin uzulnuğunu giriniz:",))

parola = ""

for i in range(uzunluk):
    parola = parola + random.choice(karakter)

print("şifreniz:",parola)
