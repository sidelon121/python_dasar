#string
nama = ["Andi", "Budi", "Cici", "Dodi"]
print(nama)

nama.append("Eka") #menambahkan data di akhir list
print(nama)
nama.insert(1, "Bambang") #menambahkan data di index tertentu
print(nama) 
nama.remove("Cici") #menghapus data berdasarkan nilai
print(nama)
nama.pop(2) #menghapus data berdasarkan index
print(nama)
del nama[0] #menghapus data berdasarkan index
print(nama) 
nama.clear() #menghapus semua data di list
print(nama)

#integer
angka = [1, 2, 3, 4, 5]
print(angka)
angka.reverse() #membalik urutan data di list
print(angka)
angka.sort() #mengurutkan data di list secara ascending
print(angka)
angka.sort(reverse=True) #mengurutkan data di list secara descending
print(angka)
print(len(angka)) #menampilkan jumlah data di list
print(min(angka)) #menampilkan nilai terkecil di list
print(max(angka)) #menampilkan nilai terbesar di list
print(sum(angka)) #menampilkan jumlah total nilai di list
print(3 in angka) #mengecek apakah nilai ada di list
print(10 in angka) #mengecek apakah nilai ada di list
print(3 not in angka) #mengecek apakah nilai tidak ada di list
print(10 not in angka) #mengecek apakah nilai tidak ada di list
print(angka.index(3)) #menampilkan index dari nilai tertentu
print(angka.count(3)) #menampilkan jumlah kemunculan nilai tertentu di list
angka2 = angka.copy() #mengcopy list ke list baru
print(angka2)
angka3 = angka + [6, 7, 8] #menggabungkan dua
print(angka3) #menampilkan hasil penggabungan list
angka4 = angka * 2 #menggandakan isi list
print(angka4)
print(angka[0]) #menampilkan data di index 0
print(angka[1]) #menampilkan data di index 1


#capuran 
data = [1, "Andi", 2.5, True, [1, 2, 3]]
print(data)
print(data[4]) #menampilkan data di index 4
print(data[4][1]) #menampilkan data di index 1 dari list di index 4
data[1] = "Budi" #mengubah data di index tertentu
print(data)
data[4].append(4) #menambahkan data di list di index 4
print(data)
data[4].remove(2) #menghapus data di list di index 4
print(data)
data[4][0] = 10 #mengubah data di list di index 4
print(data)
data[4].sort() #mengurutkan data di list di index 4
print(data)
data[4].reverse() #membalik urutan data di list di index 4
print(data)
data[4].clear() #menghapus semua data di list di index 4
print(data)
data.clear() #menghapus semua data di list
print(data)
