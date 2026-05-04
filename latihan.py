# print("=== Level 1 ===")

# print("--- Latihan 1 ---")
# for i in range(1, 6):
#     print(i)
    
# print("--- Latihan 2 ---")
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
        
# print("--- Latihan 3 ---")
# angka = int(input("Masukan sebuah angka:"))
# if angka > 0:
#     print("Angka tersebut positif")
# elif angka < 0:
#     print("Angka tersebut negatif")
# else:
#     print("Angka tersebut nol")


# print("=== Level 2 ===")

# print(" Tantangan 1 ")
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(f"{i} adalah Ganjil")
#     else:
#         print(f"{i} adalah Genap")
        
# print(" Tantangan 2 ")
# angka = int(input("Masukkan angka: "))
# total = 0
# teks = ""
# for i in range(1, angka + 1):
#     total = total + i
#     teks = teks + str(i) 
#     if i < angka:
#         teks = teks + " + "
# print(teks)
# print("Hasilnya adalah:", total)

# print(" Tantangan 3 ")
# for i in range(1, 5):
#     print("*" * i)

# teks = ""
# angka = 5
# for i in range(angka, 0, -1):
#     teks = teks + str(i) 
#     if i > 1:
#         teks = teks + " + "
# print(teks)




# total = 0
# angka = []
# for i in range(2, 11, 2):
#     total += i
#     angka.append(str(i))
# teks = " + ".join(angka)
# print(f"{teks} = {total}")

# limit = int(input("Masukkan angka: "))
# total = 0
# angka = []
# for i in range(1, limit + 1, 2):
#     total += i    
#     angka.append(str(i))
# teks = " + ".join(angka)
# print(f"{teks} = {total}")
    
# limit = int(input("Masukkan angka: "))
# total = 0
# angka = []
# if limit % 2 == 0:
#     limit -= 1

# for i in range(limit, 0, -2):
#     total += i
#     angka.append(str(i))

# teks = " + ".join(angka)
# print(f"{teks} = {total}")

# total = 0
# teks = ""

# for i in range(1, 6):
#     total += i 
#     if i == 1:
#         teks += str(i)
#     else:
#         teks += "+" + str(i)
# print(f"{teks} = {total}")


total = 0
teks = ""
jumlah = 0
rata_rata = 0
input_angka = int(input("Masukkan angka: "))
for i in range(2, input_angka + 1, 2):
    total += i
    jumlah += 1
    if i == "":
        teks += str(i)
    else: 
        teks += "+" + str(i)
print(f"{teks} = {total}")
print(f"Jumlah angka genap: {jumlah} ")
if jumlah > 0:
    rata_rata = total / jumlah
    print(f"Rata-rata angka genap: {rata_rata}")