print("=== SIMPAN DATA KE FILE ===")
file = open("data.txt", "w")
while True:
    nama = input("Masukkan nama: ")
    if nama == "":
        break
    umur = input("Masukkan umur: ")
    file.write(nama + ", " + umur + "\n")
    print("Data tersimpan.")
    print("langsung enter untuk selesai")
file.close()
print("Data berhasil disimpan ke file data.txt")

print("=== BACA DATA DARI FILE ===")
try:
    with open("data.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            print("Nama:", data[0], ", Umur:", data[1])
except FileNotFoundError:
    print("File tidak ditemukan.")
print("=== data selesai dibaca ===")