import sys
import math

# ========================
# Fungsi Dasar
# ========================
def keluar():
    print("\n=== Terima kasih sudah menggunakan kalkulator lengkap ini. ===")
    print("=== Sampai jumpa lagi! ===")
    sys.exit()

def lanjut():
    lanjut = input("\nTekan '#' lalu Enter untuk keluar atau tekan Enter untuk melanjutkan... ")
    if lanjut.strip() == "#":
        keluar()

# ========================
# Operasi Matematika Dasar
# ========================
def app_penjumlahan():
    try:
        print("\n=== Operasi Penjumlahan ===")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = int(a) + int(b)
        print(f"Hasil dari {a:.0f} + {b:.0f} = {hasil}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_pengurangan():
    try:
        print("\n=== Operasi Pengurangan ===")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = int(a) - int(b)
        print(f"Hasil dari {a:.0f} - {b:.0f} = {hasil}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_perkalian():
    try:
        print("\n=== Operasi Perkalian ===")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = int(a) * int(b)
        print(f"Hasil dari {a:.0f} x {b:.0f} = {hasil}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_pembagian():
    try:
        print("\n=== Operasi Pembagian ===")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        if b == 0:
            print("Tidak bisa membagi dengan nol.")
        else:
            hasil = int(a) / int(b)
            print(f"Hasil dari {a:.0f} / {b:.0f} = {hasil:.2f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

# ========================
# Operasi Tambahan
# ========================
def app_pangkat():
    try:
        print("\n=== Operasi Pangkat ===")
        a = float(input("Masukkan angka: "))
        b = float(input("Masukkan pangkat: "))
        hasil = int(a) ** int(b)
        print(f"Hasil dari {a:.0f} ** {b:.0f} = {hasil}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_persentase():
    try:
        print("\n=== Operasi Persentase ===")
        nilai = float(input("Masukkan nilai: "))
        total = float(input("Masukkan total: "))
        if total == 0:
            print("Total tidak boleh nol.")
        else:
            hasil = (nilai / total) * 100
            print(f"{nilai:.0f} adalah {hasil:.2f}% dari {total:.0f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

# ========================
# Fitur Tambahan
# ========================
def app_akar_kuadrat():
    try:
        print("\n=== Operasi Akar Kuadrat ===")
        a = float(input("Masukkan angka: "))
        if a < 0:
            print("Tidak bisa menghitung akar kuadrat dari angka negatif.")
        else:
            hasil = math.sqrt(a)
            print(f"Akar kuadrat dari {a:.0f} adalah {hasil:.2f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_akar_pangkat_n():
    try:
        print("\n=== Operasi Akar Pangkat-n ===")
        a = float(input("Masukkan angka: "))
        n = float(input("Masukkan nilai pangkat akar (contoh: 3 untuk akar kubik): "))
        if n == 0:
            print("Nilai pangkat akar tidak boleh nol.")
        elif a < 0 and n % 2 == 0:
            print("Tidak bisa menghitung akar genap dari angka negatif.")
        else:
            hasil = a ** (1 / n)
            print(f"Akar pangkat-{n:.0f} dari {a:.0f} adalah {hasil:.4f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_modulus():
    try:
        print("\n=== Operasi Modulus (Sisa Bagi) ===")
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        if b == 0:
            print("Tidak bisa melakukan modulus dengan nol.")
        else:
            hasil = int(a) % int(b)
            print(f"Sisa bagi dari {a:.0f} % {b:.0f} = {hasil}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

def app_logaritma():
    try:
        print("\n=== Operasi Logaritma (Basis 10) ===")
        a = float(input("Masukkan angka: "))
        if a <= 0:
            print("Logaritma hanya bisa untuk angka > 0.")
        else:
            hasil = math.log10(a)
            print(f"Logaritma basis 10 dari {a:.0f} adalah {hasil:.4f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

# ========================
# Trigonometri
# ========================
def app_trigonometri():
    try:
        print("\n=== Operasi Trigonometri ===")
        print("1. sin")
        print("2. cos")
        print("3. tan")
        pilih = input("Pilih fungsi (1/2/3): ").strip()
        sudut = float(input("Masukkan sudut dalam derajat: "))
        rad = math.radians(sudut)

        if pilih == "1":
            hasil = math.sin(rad)
            nama = "sin"
        elif pilih == "2":
            hasil = math.cos(rad)
            nama = "cos"
        elif pilih == "3":
            hasil = math.tan(rad)
            nama = "tan"
        else:
            print("Pilihan tidak valid.")
            return lanjut()

        print(f"Hasil {nama}({sudut}°) = {hasil:.6f}")
    except ValueError:
        print("Input tidak valid.")
    lanjut()

# ========================
# Menu Utama
# ========================
def app_menu():
    print("=== KALKULATOR LENGKAP ===")
    while True:
        print("\nPilih operasi:")
        print("[+] Penjumlahan")
        print("[-] Pengurangan")
        print("[x] Perkalian")
        print("[/] Pembagian")
        print("[**] Pangkat")
        print("[%] Persentase")
        print("[√] Akar kuadrat")
        print("[akar] Akar pangkat-n")
        print("[mod] Modulus (sisa bagi)")
        print("[log] Logaritma (basis 10)")
        print("[trig] Trigonometri (sin, cos, tan)")
        print("[#] Keluar")

        operasi = input("Masukkan pilihan: ").strip().lower()
        while operasi == "":
            operasi = input("Masukan pilihan terlebih dahulu! ")

        if operasi == "+":
            app_penjumlahan()
        elif operasi == "-":
            app_pengurangan()
        elif operasi == "x":
            app_perkalian()
        elif operasi == "/":
            app_pembagian()
        elif operasi == "**":
            app_pangkat()
        elif operasi == "%":
            app_persentase()
        elif operasi == "√":
            app_akar_kuadrat()
        elif operasi == "akar":
            app_akar_pangkat_n()
        elif operasi == "mod":
            app_modulus()
        elif operasi == "log":
            app_logaritma()
        elif operasi == "trig":
            app_trigonometri()
        elif operasi == "#":
            keluar()
        else:
            print("Operasi tidak valid. Silakan masukkan dari daftar di atas.")

app_menu()
