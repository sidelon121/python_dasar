hari = input("Masukkan nama hari: ")
match hari:
    case "Senin"|"Selasa"|"Rabu"|"Kamis"|"Jumat":
        print("Hari sekolah")
    case "Sabtu"|"Minggu":
        print("hari libur")
    case _:
        print("Hari tidak valid")    