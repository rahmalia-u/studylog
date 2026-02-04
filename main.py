from datetime import datetime, timedelta

catatan = []

def tambah_catatan():
    """Menambahkan catatan belajar baru ke dalam list"""
    print("\n--- Tambah Catatan Belajar ---")
    
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel/mata pelajaran: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    
    # Membuat catatan dalam bentuk dictionary
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
        "tanggal": datetime.now().strftime("%Y-%m-%d")
    }
    
    # Menyimpan ke list catatan
    catatan.append(catatan_baru)
    
    print(f"✓ Catatan '{topik}' berhasil ditambahkan!")


def lihat_catatan():
    """Menampilkan semua catatan belajar"""
    print("\n--- Daftar Catatan Belajar ---")
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("Belum ada catatan. Mulai tambahkan catatan belajar Anda!")
        return
    
    # Menampilkan semua catatan
    for i, item in enumerate(catatan, 1):
        print(f"\n{i}. Mapel: {item['mapel']}")
        print(f"   Topik: {item['topik']}")
        print(f"   Durasi: {item['durasi']} menit")
        print(f"   Tanggal: {item['tanggal']}")
        print("   " + "-" * 35)

def total_waktu():
    """Menghitung total durasi belajar dari semua catatan"""
    print("\n--- Total Waktu Belajar ---")
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("Belum ada catatan. Mulai tambahkan catatan belajar Anda!")
        return
    
    # Menghitung total durasi
    total = 0
    for item in catatan:
        total += item['durasi']
    
    # Mengubah menit menjadi jam dan menit
    jam = total // 60
    menit = total % 60
    
    print(f"\nTotal waktu belajar: {total} menit")
    print(f"Atau: {jam} jam {menit} menit")
    print(f"Rata-rata per catatan: {total // len(catatan)} menit")

def ringkasan_mingguan():
    """Menampilkan ringkasan belajar minggu ini"""
    print("\n--- Ringkasan Mingguan ---")
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("Belum ada catatan. Mulai tambahkan catatan belajar Anda!")
        return
    
    # Menghitung tanggal minggu ini (7 hari terakhir)
    hari_ini = datetime.now()
    tujuh_hari_lalu = hari_ini - timedelta(days=7)
    
    # Filter catatan minggu ini
    catatan_minggu = []
    for item in catatan:
        tanggal_catatan = datetime.strptime(item['tanggal'], "%Y-%m-%d")
        if tanggal_catatan >= tujuh_hari_lalu:
            catatan_minggu.append(item)
    
    # Jika tidak ada catatan minggu ini
    if len(catatan_minggu) == 0:
        print("Belum ada catatan minggu ini.")
        return
    
    # Menghitung total per mapel
    mapel_dict = {}
    total_minggu = 0
    
    for item in catatan_minggu:
        mapel = item['mapel']
        if mapel not in mapel_dict:
            mapel_dict[mapel] = 0
        mapel_dict[mapel] += item['durasi']
        total_minggu += item['durasi']
    
    # Menampilkan ringkasan
    print(f"\nCatatan belajar minggu ini: {len(catatan_minggu)} catatan")
    print(f"Total waktu belajar: {total_minggu} menit ({total_minggu // 60}j {total_minggu % 60}m)")
    print("\nWaktu belajar per mapel:")
    for mapel, waktu in mapel_dict.items():
        print(f"  • {mapel}: {waktu} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Ringkasan mingguan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        ringkasan_mingguan()
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")