# menggunakan loop for untuk mencetak angka dari 0 hingga 999
for i in range(1000):
    print(i)

# menggunakan loop for untuk mencetak angka dari 1 hingga 9
for i in range(1, 10):
    print(i)
    
# menggunakan loop for untuk mencetak angka dari 1 hingga 9 dengan langkah 2
for i in range(1, 10, 2):
    print(i)
    
# menggunakan loop for untuk mencetak "Saya suka Python" sebanyak 100 kali
for i in range(100):
    print("Saya suka Python")
    
# menghitung minimal, maksimal, dan jumlah dari sebuah list angka
angka = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Nilai minimal:", min(angka))
print("Nilai maksimal:", max(angka))
print("Jumlah:", sum(angka))

# mengitung mundur dari 10 hingga 1
for i in range(10, 0, -1):
    print(i)