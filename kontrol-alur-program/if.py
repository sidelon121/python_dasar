# contoh penggunaan if
angka = int(input("Masukkan angka: "))
if angka > 0:
    print("Angka positif")  
if angka < 0:
    print("Angka negatif")
if angka == 0:
    print("Angka nol")
    

# contoh penggunaan if...else
nilai = int(input("Masukkan nilai: "))
if nilai >= 80:
    print("Anda lulus dengan nilai B")
else:
    print("Anda tidak lulus")
    

# contoh penggunaan if...elif...else
nilai = int(input("Masukkan nilai: "))
if nilai >= 90:
    print("Anda lulus dengan nilai A")
elif nilai >= 80:
    print("Anda lulus dengan nilai B")
elif nilai >= 70:
    print("Anda lulus dengan nilai C")
else:
    print("Anda tidak lulus")
    
    