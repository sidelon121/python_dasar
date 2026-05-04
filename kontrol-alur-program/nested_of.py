username = input("Masukkan username: ")
password = input("Masukkan password: ")
if username == "admin":
    if password == "12345":
        print("Login berhasil")
        print("Selamat datang, admin!")
    else:
        print("password salah")
else:
    print("username tidak ditemukan")
    print("Silakan coba lagi.")