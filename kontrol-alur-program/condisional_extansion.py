nama = int(input("Masukkan angka: "))
umur = "kurang dari 17" + " " + "belum punya KTP"if nama < 17 else "lebih dari 17" + " " + "sudah punya KTP"
print(f"Angka {nama} adalah {umur}")