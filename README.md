# Labpy03
Nama    : Diajeng triana k.

Nim     : 312110474

Matkul  : Bahasa pemrogaman

# LOOPING
- LOOPING sendiri artinya perulangan,dalam bahasa pemrograman merupakan suatu pernyataan untuk mengintruksi komputer agar melakukan sesuatu secara berulang.
- Terdapat 2 jenis perulangan dalam bahasa pemrograman python ,yaitu perulangan for & while . Berikut contoh dari program looping pada python.

# Algoritma latihan1.py

print ("masukkan nilai N: 5")

import random

j = 6

a = 0

for i in range(j):
    i = random.uniform(.0, .5)
    a += 1
    print("data ke :", a, "==>", i)

print("Selesai")

1. "print" : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.

2. "import" : fungsi lanjut yang dipanggil oleh statement import.

3. "random" : untuk menentukan suatu pilihan.

4. "range" : merupakan fungsi yang menghasilkan list. Fungsi ini akan menciptakan sebuah list baru dengan rentang nilai tertentu.

5. "uniform": digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y.

# Screenshoot hasil output latihan1.py

<img width="726" alt="hasil output latihan1" src="https://user-images.githubusercontent.com/92905452/140963273-8b744b40-c018-407b-afb1-2b5eefff82c1.png">

# Algoritma latihan2.py

maks = 0

while True:
    
    a = int(input("Masukkan bilangan = "))
    
    if maks < a:
        maks = a
    if a == 0:
        break

print("Bilangan terbesarnya Adalah = ", maks)

1. "max" : fungsi bulid-in untuk mencari nilai tertinggi. Fungsi ini dapat diberikan sebuah parameter berupa angka.

2. "while" : disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.

3. "int" : berfungsi mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer).

4. "if" = Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu.

5. "input" : masukan yang kita berikan ke program.

6. "break" : fungsi yang menghentikan operasi dibawahnya jika suatu kondisi yang ditentukan telah tercapai.

7. "print" : berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks.

# Screenshoot hasil output latihan2.py

