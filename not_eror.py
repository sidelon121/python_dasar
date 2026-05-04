print("=== KALKULATOR SEDERHANA ===")
try:
    while True:
        print("Pilih operasi:")
        print("+") 
        print("-")
        print("x")
        print("/")
        operasi = input("Masukkan pilihan: ")
        if operasi not in ["+", "-", "x", "/"]:
            print("Pilihan operasi tidak valid.")
            break
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        if operasi == "+":
            print("=== operasi penjumlahan ===")
            hasil = int(angka1) + int(angka2)
            print("Hasil penjumlahan:", hasil)
        elif operasi == "-":
            print("=== operasi pengurangan ===")
            hasil = int(angka1) - int(angka2)
            print("Hasil pengurangan:", hasil)
        elif operasi == "x":
            print("=== operasi perkalian ===")  
            hasil = int(angka1) * int(angka2)
            print("Hasil perkalian:", hasil)
        elif operasi == "/":
            if angka2 == 0:
                print("Tidak bisa membagi dengan nol.")
            else:
                hasil = int(angka1) / int(angka2)
                print("Hasil pembagian:", hasil)
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")
except:
    print("Terjadi kesalahan.")
print("Perhitungan selesai, terima kasih sudah menggunakan kalkulator sederhana ini.")


try:    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
else: 
    print("=== Menentukan Jenis Angka ===")
    if angka > 0:
        print("Angka positif")  
    if angka < 0:
        print("Angka negatif")
    if angka == 0:
        print("Angka nol")
finally:
    print("Proses penentuan jenis angka selesai.")