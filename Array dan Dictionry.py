data = []

while True:
    print("\n1.Tambah  2.Lihat  3.Cari  4.Keluar")
    p = input("Pilih: ")

    if p == "1":
        d = {"nama": input("Nama: "),
             "umur": int(input("Umur: ")),
             "jurusan": input("Jurusan: "),
             "nilai": float(input("Nilai: "))}
        data.append(d)

    elif p == "2":
        if not data: print("Belum ada data.")
        else:
            print(f"\n{'No':<3}{'Nama':<12}{'Umur':<6}{'Jurusan':<15}{'Nilai':<6}")
            print("-"*45)
            for i,m in enumerate(data,1):
                print(f"{i:<3}{m['nama']:<12}{m['umur']:<6}{m['jurusan']:<15}{m['nilai']:<6}")

    elif p == "3":
        n = input("Cari nama: ").lower()
        for m in data:
            if m["nama"].lower() == n:
                print(f"{m['nama']} ({m['jurusan']}) - Nilai: {m['nilai']}")
                break
        else:
            print("Tidak ditemukan.")
    elif p == "4":
        break