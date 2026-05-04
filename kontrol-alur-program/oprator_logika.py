umur = int(input("Masukkan umur: "))
punya_SIM = input("Apakah anda punya SIM (ya/tidak): ").lower()
umur >= 17 and punya_SIM == "ya"
print("Boleh mengemudi") if umur >= 17 and punya_SIM == "ya" else print("Tidak boleh mengemudi")