#break 
angka_rahasia = 21
while True:
    angka_tebakan = int(input("Masukkan angka tebakan Anda: "))
    if angka_tebakan == angka_rahasia:
        print("Tebakan Anda benar!")
        break
    elif angka_tebakan < angka_rahasia:
        print("Tebakan Anda terlalu rendah.")
    else:
        print("Tebakan Anda terlalu tinggi.")
    print("Coba lagi!")
    
#continue
for i in range(21):
    if i % 4 != 0:
        continue
    print(f"ini angka genap: {i}")