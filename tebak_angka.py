import random

# === Variabel global untuk menyimpan leaderboard ===
leaderboard = []

def keluar():
    print("\n=== Terima kasih sudah memainkan game tebak angka ini! ===")
    print("=== Sampai jumpa lagi! ===")
    tampilkan_leaderboard()
    exit()

def tampilkan_leaderboard():
    if not leaderboard:
        print("\nBelum ada skor di leaderboard.")
        return

    print("\n🏆 LEADERBOARD TOP 5 🏆")
    print("=" * 30)
    sorted_board = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:5]
    for i, (nama, skor) in enumerate(sorted_board, start=1):
        print(f"{i}. {nama} - {skor} poin")
    print("=" * 30)

def main_game(nama, batas_angka, maksimal_tebakan):
    try:
        angka_acak = random.randint(1, batas_angka)
        tebakan = 0
        skor = 0

        print(f"\nTebak angka antara 1 hingga {batas_angka}")
        print(f"Kamu punya {maksimal_tebakan} kesempatan.\n")

        while tebakan < maksimal_tebakan:
            tebakan += 1
            try:
                angka_user = int(input(f"Tebakan ke-{tebakan}: "))
            except ValueError:
                print("⚠️ Input tidak valid. Harap masukkan angka!")
                continue

            if angka_user > angka_acak:
                print("Angka tebakan terlalu besar.")
            elif angka_user < angka_acak:
                print("Angka tebakan terlalu kecil.")
            else:
                print("🎉 Selamat! Angka kamu BENAR! 🎯")
                # Skor lebih tinggi jika menebak dengan cepat
                skor = (maksimal_tebakan - tebakan + 1) * 10
                print(f"Kamu mendapatkan {skor} poin!\n")
                leaderboard.append((nama, skor))
                break

            if tebakan == maksimal_tebakan:
                print("\n😢 Kesempatan habis!")
                print(f"Angka yang benar adalah {angka_acak}.\n")

        lanjut = input("Tekan # lalu Enter untuk keluar, atau Enter untuk lanjut... ")
        if lanjut.strip() == "#":
            keluar()

    except Exception as e:
        print("Terjadi kesalahan:", e)

def app_menu():
    print("*** 🎮 GAME TEBAK ANGKA 🎮 ***")

    nama = input("Masukkan nama kamu: ").strip()
    if not nama:
        nama = "Pemain"

    while True:
        print("\n=== PILIH LEVEL ===")
        print("1. Mudah (1–10, 3 tebakan)")
        print("2. Menengah (1–30, 4 tebakan)")
        print("3. Sulit (1–50, 5 tebakan)")
        print("4. Sangat Sulit (1–100, 7 tebakan)")
        print("5. Lihat Leaderboard")
        print("#. Keluar")

        pilihan = input("Masukkan pilihan level: ").strip()

        if pilihan == "1":
            main_game(nama, 10, 3)
        elif pilihan == "2":
            main_game(nama, 30, 4)
        elif pilihan == "3":
            main_game(nama, 50, 5)
        elif pilihan == "4":
            main_game(nama, 100, 7)
        elif pilihan == "5":
            tampilkan_leaderboard()
        elif pilihan == "#":
            keluar()
        else:
            print("Pilihan tidak valid, masukan pilihan dengan benar!")

# Jalankan program
app_menu()
