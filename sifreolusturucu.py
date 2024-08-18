import random 

while True:
    lib = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ("")
    sifre_long = int(input("Şife uzunluğu gir(Sadece rakam girin örn:1,2,3,4,5):"))
    for i in range(sifre_long):
        sifre += random.choice(lib)
    print(sifre)
