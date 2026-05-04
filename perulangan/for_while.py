#for else
nama = input("Siapa nama Anda? ")
data = ["ANDI", "BUDI", "CACA", "DODO", "EKA"]
username_dicari = input("Masukkan username yang ingin Anda cari: ").upper()      
for username in data:
    if username == username_dicari:
        print(f"Username {username_dicari} ditemukan!")
        break   
else:
    print(f"Username {username_dicari} tidak ditemukan.")
    
#while else
password = "1234"
percobaan = 0
maks_percobaan = 3
while percobaan < maks_percobaan:
    masukan = input("Masukkan password: ")
    if masukan == password:
        print("Password benar! Akses diberikan.")
        break
    else:
        percobaan += 1
        print(f"Password salah! Anda memiliki {maks_percobaan - percobaan} percobaan lagi.")
else:
    print("Anda telah mencoba terlalu banyak kali. Akses ditolak.")