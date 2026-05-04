#operator aritmatika
a = 21
b = 15
c = a + b #penjumlahan
d = a - b  #pengurangan
e = a * b #perkalian
f = a / b #pembagian dengan sisa
g = a // b #pembagian tanpa sisa
h = a % b  #sisa bagi
i = a ** b # pangkat
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)    

#operator penugasan
x = 66
print(x) #menampilkan nilai x
x += 4  #x = x + 4  #penjumlahan
print(x) #menampilkan nilai x
x -= 4  #x = x - 4  #pengurangan
print(x) #menampilkan nilai x   
x *= 4  #x = x * 4  #perkalian
print(x) #menampilkan nilai x
x /= 4  #x = x / 4  #pembagian dengan sisa
print(x) #menampilkan nilai x
x //= 4  #x = x // 4 #pembagian tanpa sisa
print(x) #menampilkan nilai x
x %= 4  #x = x % 4 #sisa bagi
print(x) #menampilkan nilai x
x **= 4  #x = x ** 4 #pangkat
print(x) #menampilkan nilai x

#operator perbandingan
a = 19
b = 33
print(a == b) #sama dengan
print(a != b) #tidak sama dengan
print(a < b)  #kurang dari
print(a > b)  #lebih dari
print(a <= b) #kurang dari sama dengan
print(a >= b) #lebih dari sama dengan

c = "Bechkam"
d = "Bechkam"
e = "Ronaldo"
print(c is d) #identitas sama dengan
print(e is not d) #identitas tidak sama dengan
print(d in e) #keanggotaan in
print(c not in e) #keanggotaan not in

#operator logika
umur = 23
print(umur > 17 and umur < 30) #and

hari = "sabtu"
print(hari == "minggu" or hari == "sabtu" ) #or

aktif = False
print(not aktif) 

#operator string
nama_depan = "Bechkam"
nama_belakang = "Putra"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

greeting = "Hello " * 3
print(greeting)

garis = "=" * 20
print(garis)

kalimat = "Saya menonton bola"
print("bola" in kalimat) #keanggotaan in    
print("sepakbola" in kalimat) #keanggotaan in
print("sepakbola" not in kalimat) #keanggotaan not in       
print(kalimat is "Saya menonton bola") #identitas sama dengan
print(kalimat is not "Saya menonton bola") #identitas tidak sama dengan

#prioritas operator
a = 10 + 5 * 2
print(a) #menampilkan hasil 10 + (5 * 2)
b = (10 + 5) * 2
print(b) #menampilkan hasil (10 + 5) * 2
c = 10 + 5 * 2 ** 2
print(c) #menampilkan hasil 10 + (5 * (2 ** 2))
d = (10 + 5 * 2) ** 2
print(d) #menampilkan hasil (10 + (5 * 2)) ** 2     
e = ((10 + 5) * 2) ** 2
print(e) #menampilkan hasil ((10 + 5) * 2) ** 2
print("prioritas operator: () **, *, /, //, %, +, -, <, <=, >, >=, ==, !=, in, not in, is, is not, not, and, or")