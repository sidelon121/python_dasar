# ...existing code...
import random

def ambil_soal(path="bank_soal.txt"):
    soal_list = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if not s:
                    continue
                parts = s.split('#')
                if len(parts) != 2:
                    continue
                kiri, kunci = parts[0].strip(), parts[1].strip().upper()
                segs = [seg.strip() for seg in kiri.split('|')]
                if len(segs) < 5:
                    # minimal: soal + 4 pilihan
                    continue
                teks_soal = segs[0]
                raw_choices = segs[1:5]  # ambil 4 pilihan pertama
                # ekstrak teks pilihan (buang "A.", "B.", dll.)
                orig_map = {}
                for rc in raw_choices:
                    lbl, sep, txt = rc.partition('.')
                    if sep == '':
                        # fallback kalau pakai format lain
                        lbl = rc.split()[0].rstrip(').')
                        txt = rc[len(lbl):].lstrip('). ').strip()
                    orig_map[lbl.strip().upper()] = txt.strip()
                # dapatkan teks jawaban benar berdasarkan kunci
                correct_text = orig_map.get(kunci)
                if correct_text is None:
                    # jika kunci tidak cocok, lewati soal
                    continue
                # simpan soal: teks_soal, list pilihan (teks), teks jawaban benar
                choices_texts = [orig_map.get(l) for l in sorted(orig_map.keys())]
                # jika beberapa label hilang, gunakan raw_choices sebagai fallback
                if any(c is None for c in choices_texts):
                    choices_texts = [rc.partition('.')[2].strip() if '.' in rc else rc for rc in raw_choices]
                soal_list.append((teks_soal, choices_texts, correct_text))
        return soal_list
    except FileNotFoundError:
        print("Error: File bank_soal.txt tidak ditemukan!")
        return []

def buat_soal(semua_soal, jumlah=10):
    if not semua_soal:
        return []
    random.shuffle(semua_soal)
    selected = semua_soal[:min(jumlah, len(semua_soal))]
    # untuk tiap soal, acak pilihan dan perbarui kunci (A-D)
    prepared = []
    for teks_soal, choices_texts, correct_text in selected:
        choices = choices_texts[:]  # salinan
        random.shuffle(choices)
        labels = ['A', 'B', 'C', 'D']
        labeled = list(zip(labels, choices))
        # cari label baru yang sesuai dengan correct_text
        new_key = None
        for lbl, txt in labeled:
            if txt == correct_text:
                new_key = lbl
                break
        # jika tidak ditemukan (aman), set None
        prepared.append({
            "soal": teks_soal,
            "choices": labeled,        # list of (label, text)
            "kunci": new_key
        })
    return prepared

def tampilkan_soal(soal_ujian):
    if not soal_ujian:
        print("Tidak ada soal yang dapat ditampilkan!")
        return
    print("\n=== SOAL UJIAN ===")
    for i, item in enumerate(soal_ujian, start=1):
        print(f"{i}. {item['soal']}")
        for lbl, txt in item['choices']:
            print(f"   {lbl}. {txt}")

def jawab_soal(soal_ujian):
    if not soal_ujian:
        return 0, 0
    benar = 0
    total = len(soal_ujian)
    for i, item in enumerate(soal_ujian, start=1):
        print(f"\nSoal {i}: {item['soal']}")
        for lbl, txt in item['choices']:
            print(f"   {lbl}. {txt}")
        jaw = input("Jawaban (A/B/C/D): ").strip().upper()
        while jaw not in ['A', 'B', 'C', 'D']:
            jaw = input("Masukkan jawaban yang valid (A/B/C/D): ").strip().upper()
        if item['kunci'] is not None and jaw == item['kunci']:
            benar += 1
            print("Jawaban benar!")
        else:
            print(f"Jawaban salah! Jawaban yang benar adalah {item['kunci']}")
    return benar, total

if __name__ == '__main__':
    print("=== PROGRAM UJIAN SEDERHANA ===")
    semua = ambil_soal("bank_soal.txt")
    soal_ujian = buat_soal(semua, jumlah=10)
    if soal_ujian:
        tampilkan_soal(soal_ujian)
        print("\nMari mulai menjawab soal!")
        benar, total = jawab_soal(soal_ujian)
        nilai = (benar / total) * 100 if total > 0 else 0
        print("\n=== HASIL UJIAN ===")
        print(f"Jawaban benar: {benar} dari {total} soal")
        print(f"Nilai akhir: {nilai:.2f}")