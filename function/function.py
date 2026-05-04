def nama_function():
    print("Ini adalah fungsi tanpa parameter dan tanpa nilai kembalian")
nama_function()

# Function dengan parameter
def fungsi_dengan_parameter(nama):
    print("Halo, " + nama + "!")
fungsi_dengan_parameter("John")

# Function dengan nilai kembalian
def luas_persegi(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi dengan sisi 4 adalah:", luas)
luas_persegi(5, 12)

# Function dengan return value
def hitung_luas_persegi(sisi):
    return sisi * sisi  
print("Luas persegi dengan sisi 4 adalah:", hitung_luas_persegi(4))
hitung_luas_persegi

def hitung_keliling_segitiga(radius):
    return 2 * 3.14 * radius    
print("Keliling segitiga dengan radius 7 adalah:", hitung_keliling_segitiga(7))
hitung_keliling_segitiga

# Function dengan parameter default
def greet(nama, pesan="Selamat datang!"):
    print(pesan + ", " + nama + "!")
greet("Alice")
greet("Bob", "Halo")

# Function dengan keyword arguments
def info_mahasiswa(nama, umur, jurusan):
    print("Nama:", nama)
    print("Umur:", umur)
    print("Jurusan:", jurusan)
info_mahasiswa(umur=21, nama="Charlie", jurusan="Informatika")

def info_profil(nama, umur, hobi, kota="Bandung", pekerjaan="Mahasiswa"):
    print(f"== Profil {nama} ==")
    print("Umur:", umur, "tahun")
    print("Kota:", kota)
    print("Hobi:", hobi)
    print("Pekerjaan:", pekerjaan)
info_profil("Dina", 22, hobi="Membaca")
info_profil("Eka", 25, kota="Jakarta", hobi="Bersepeda", pekerjaan="Insinyur")

# Function dengan local variable
def fungsi_local():
    x = 10  # Variabel lokal
    print("Nilai x di dalam fungsi:", x)
fungsi_local()
# print(x)  # Ini akan menghasilkan error karena x tidak dapat diakses di luar fungsi

# Function dengan global variable
y = 20  # Variabel global
def fungsi_global():
    global y
    y = 30  # Mengubah nilai variabel global
    print("Nilai y di dalam fungsi:", y)
fungsi_global()
print("Nilai y di luar fungsi:", y)
# Menggunakan variabel global tanpa mengubahnya
def fungsi_global_tanpa_ubah():
    global y
    y = 20  # Menggunakan nilai global tanpa mengubahnya
    print("Nilai y di dalam fungsi:", y)
fungsi_global_tanpa_ubah()

# Function dengan parameter dinamis
def jumlahkan(*angka):
    total = 0
    for num in angka:
        total += num
    return total
print("Jumlahkan 1, 2, 3:", jumlahkan(1, 2, 3))
jumlahkan

def kalikan(**angka):
    total = 1
    for num in angka.values():
        total *= num
    return total
print("Kalikan 2, 3, 4:", kalikan(a=2, b=3, c=4))
kalikan

def gabungkan(*args, **kwargs):
    hasil = "Args:\n" + "\n".join(map(str, args)) + "\nKwargs:\n" + "\n".join(f"{k}: {v}" for k, v in kwargs.items())
    return hasil
print(gabungkan(1, 2, 3, nama="Fajar", umur=30))
gabungkan


def cetak_list(*args):
    for item in args:
        print(item)
cetak_list("apel", "pisang", "jeruk")
cetak_list("mangga", "kiwi", "semangka")

def cetak_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
cetak_dict(nama="Gina", umur=28, kota="Surabaya")
cetak_dict(merek="Toyota", model="Camry", tahun=2020)   
cetak_dict
def gabungkan(*args, **kwargs):
    hasil = "Args:\n" + "\n".join(map(str, args)) + "\nKwargs:\n" + "\n".join(f"{k}={v}" for k, v in kwargs.items())
    print(hasil)
gabungkan(1, 2, 3, nama="Fajar", umur=30)
