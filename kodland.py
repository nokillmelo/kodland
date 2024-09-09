import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
hane = int(input("sifreniz kac haneli olsun:"))
sifre = ""
for i in range(hane):
    y = random.choices(x)
    sifre += y
    print(sifre)
