#manipulasi string
name = "Ramon"  #string
umur = 26   #integer
pesan = "nama dia " + name + ", umur dia " + str(umur)  #menggabungkan string dan integer
print(pesan) #menggabungkan string dan integer
print(len(name))    #menghitung panjang karakter
print(len(pesan))  #menghitung panjang karakter

#akses karakter
name = "Tanque"
print(name[0]) #mengambil karakter ke 0
print(name[1]) #mengambil karakter ke 1
print(name[2]) #mengambil karakter ke 2

print(name[-1]) #mengambil karakter ke -1
print(name[-2]) #mengambil karakter ke -2
print(name[-3]) #mengambil karakter ke -3

#slicing
name = "Barros"
print(name[0:3]) #mengambil karakter ke 0 sampai 3
print(name[3:6]) #mengambil karakter ke 3 sampai 6
print(name[:]) #mengambil semua karakter

name = "Haye"
print(name.lower()) #mengubah semua huruf menjadi kecil
print(name.upper()) #mengubah semua huruf menjadi kapital

name = "thom haye"
print(name.title()) #mengubah huruf pertama di setiap kata menjadi kapital
print(name.capitalize()) #mengubah huruf pertama menjadi kapital
print(name.replace("haye", "Delon")) #mengganti kata haye menjadi Delon

name = "     Haye     "
print(name.strip()) #menghilangkan spasi di kiri dan kanan
print(name.lstrip()) #menghilangkan spasi di kiri
print(name.rstrip()) #menghilangkan spasi di kanan

name = "Farhan Akmal"
print(count := name.count("a"))   #menghitung jumlah karakter a

kalimat = "Saya suka menonton bola"
print(kalimat.split()) #memecah kalimat menjadi list
print(kalimat.find("bola")) #mencari kata bola dalam kalimat
print(kalimat.find("sepakbola")) #mencari kata sepakbola dalam kalimat
print(kalimat.index("suka")) #mencari kata suka dalam kalimat

#karakter khusus
kalimat = "saya suka menonton bola,\n tapi saya tidak bisa bermain bola"
print(kalimat) #menampilkan kalimat dengan enter
print(kalimat.splitlines()) #memecah kalimat menjadi list dengan enter

data = "nama:\tFarhan Akmal\numur:\t17 tahun"
print(data) #menampilkan data

lokasi = "C:\\User\\Farhan"
print(lokasi) #menampilkan lokasi dengan backslash  

kalimat = "Saya suka menonton bola \"Liga Inggris\""
print(kalimat) #menampilkan kalimat dengan tanda petik

#f-string

name = "Bechkam Putra Nugraha"
umur = 23
alamat = "Bandung"
pesan = f"nama dia {name}, umur dia {umur}, alamat dia di {alamat}"  #menggabungkan string dan integer dengan f-string
print(pesan) #menggabungkan string dan integer dengan f-string

goal = 10
assist = 15
jumlah = f"total gol dan assistnya adalah {goal + assist}" #menggabungkan string dan operasi matematika dengan f-string
print(jumlah) #menampilkan hasil penggabungan string dan operasi matematika dengan f-string

name = "Bechkam Putra Nugraha"
kalimat = f"Hello, {name}. Kamu bermain sangat baik musim ini"
print(kalimat) #menampilkan kalimat dengan f-string