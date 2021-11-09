maks = 0
while True:
    a = int(input("Masukkan bilangan = "))
    if maks < a:
        maks = a
    if a == 0:
        break
print("Bilangan terbesarnya Adalah = ", maks)