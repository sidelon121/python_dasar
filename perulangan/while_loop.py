angka = 1
while angka <= 10:
    print(angka)
    angka += 1
    
    
sandwich = " "
while sandwich != "selesai":
    sandwich = input("Masukkan nama sandwich yang diinginkan: ")
    if sandwich != "selesai":
        print(f"nama sandwich salah")
print("Terima kasih! Pesanan sandwich Anda sedang diproses.")