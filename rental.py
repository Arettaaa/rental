# Program Pendataan Barang Rental Event Organizer

# Daftar barang untuk menyimpan data barang yang akan diinput
daftar_barang = []

# Fungsi untuk menambahkan barang baru ke dalam daftar
def tambah_barang(nama, kategori, harga_sewa, status='Tersedia'):
    barang = {
        'Nama': nama,
        'Kategori': kategori,
        'Harga Sewa': harga_sewa,
        'Status': status
    }
    daftar_barang.append(barang)
    print(f"Barang '{nama}' berhasil ditambahkan dengan status '{status}' dan harga sewa Rp{harga_sewa}.")

# Fungsi untuk melihat semua barang yang ada di daftar
def lihat_barang():
    if not daftar_barang:
        print("Belum ada barang yang terdaftar.")
    else:
        print("\nDaftar Barang:")
        for idx, barang in enumerate(daftar_barang, start=1):
            print(f"{idx}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}, Status: {barang['Status']}")

# Fungsi untuk mengubah status barang
def ubah_status_barang(nama, status_baru):
    for barang in daftar_barang:
        if barang['Nama'].lower() == nama.lower():
            barang['Status'] = status_baru
            print(f"Status barang '{nama}' berhasil diubah menjadi '{status_baru}'.")
            return
    print(f"Barang dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk menghapus barang dari daftar
def hapus_barang(nama):
    for barang in daftar_barang:
        if barang['Nama'].lower() == nama.lower():
            daftar_barang.remove(barang)
            print(f"Barang '{nama}' berhasil dihapus.")
            return
    print(f"Barang dengan nama '{nama}' tidak ditemukan.")

# Fungsi untuk mencari barang berdasarkan nama atau kategori
def cari_barang(keyword):
    hasil_cari = [barang for barang in daftar_barang if keyword.lower() in barang['Nama'].lower() or keyword.lower() in barang['Kategori'].lower()]
    if hasil_cari:
        print("\nHasil Pencarian:")
        for idx, barang in enumerate(hasil_cari, start=1):
            print(f"{idx}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}, Status: {barang['Status']}")
    else:
        print(f"Tidak ada barang dengan kata kunci '{keyword}'.")

# Fungsi untuk mengurutkan daftar barang berdasarkan nama
def urutkan_barang():
    if not daftar_barang:
        print("Belum ada barang yang terdaftar untuk diurutkan.")
    else:
        daftar_barang.sort(key=lambda x: x['Nama'])
        print("Daftar barang berhasil diurutkan berdasarkan nama.")
        lihat_barang()

# Fungsi untuk menghitung jumlah barang per kategori
def hitung_barang_per_kategori():
    kategori_count = {}
    for barang in daftar_barang:
        kategori = barang['Kategori']
        if kategori in kategori_count:
            kategori_count[kategori] += 1
        else:
            kategori_count[kategori] = 1
    
    print("\nJumlah Barang per Kategori:")
    for kategori, count in kategori_count.items():
        print(f"{kategori}: {count} barang")

# Fungsi untuk menampilkan laporan ringkas
def laporan_ringkas():
    total_barang = len(daftar_barang)
    barang_tersedia = len([barang for barang in daftar_barang if barang['Status'] == 'Tersedia'])
    barang_digunakan = len([barang for barang in daftar_barang if barang['Status'] == 'Sedang Digunakan'])
    barang_maintenance = len([barang for barang in daftar_barang if barang['Status'] == 'Maintenance'])
    
    print("\n=== Laporan Ringkas Barang Rental ===")
    print(f"Total Barang: {total_barang}")
    print(f"Barang Tersedia: {barang_tersedia}")
    print(f"Barang Sedang Digunakan: {barang_digunakan}")
    print(f"Barang Maintenance: {barang_maintenance}")

# Fungsi untuk mengekspor data ke file TXT
def ekspor_ke_txt(filename="daftar_barang.txt"):
    try:
        with open(filename, "w") as file:
            file.write("Daftar Barang Rental Event Organizer\n")
            file.write("=====================================\n\n")
            if not daftar_barang:
                file.write("Belum ada barang yang terdaftar.\n")
            else:
                for idx, barang in enumerate(daftar_barang, start=1):
                    file.write(f"{idx}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}, Status: {barang['Status']}\n")
            print(f"Data berhasil diekspor ke file '{filename}'.")
    except IOError:
        print("Terjadi kesalahan saat menulis ke file.")

# Fungsi utama untuk menampilkan menu dan menangani pilihan
def menu():
    while True:
        print("\n=== Aplikasi Pendataan Barang Rental ===")
        print("1. Tambah Barang")
        print("2. Lihat Daftar Barang")
        print("3. Ubah Status Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("6. Urutkan Barang Berdasarkan Nama")
        print("7. Hitung Barang per Kategori")
        print("8. Tampilkan Laporan Ringkas")
        print("9. Ekspor Data ke File TXT")
        print("10. Keluar")
        
        pilihan = input("Pilih menu (1-10): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama barang: ")
            kategori = input("Masukkan kategori barang: ")
            try:
                harga_sewa = int(input("Masukkan harga sewa barang: "))
            except ValueError:
                print("Harga sewa harus berupa angka.")
                continue
            tambah_barang(nama, kategori, harga_sewa)
        
        elif pilihan == '2':
            lihat_barang()
        
        elif pilihan == '3':
            nama = input("Masukkan nama barang yang ingin diubah statusnya: ")
            print("Pilih status baru:")
            print("1. Tersedia")
            print("2. Sedang Digunakan")
            print("3. Maintenance")
            status_pilihan = input("Pilih status (1-3): ")
            if status_pilihan == '1':
                status_baru = "Tersedia"
            elif status_pilihan == '2':
                status_baru = "Sedang Digunakan"
            elif status_pilihan == '3':
                status_baru = "Maintenance"
            else:
                print("Status tidak valid.")
                continue
            ubah_status_barang(nama, status_baru)
        
        elif pilihan == '4':
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            hapus_barang(nama)
        
        elif pilihan == '5':
            keyword = input("Masukkan kata kunci pencarian (nama/kategori): ")
            cari_barang(keyword)
        
        elif pilihan == '6':
            urutkan_barang()
        
        elif pilihan == '7':
            hitung_barang_per_kategori()
        
        elif pilihan == '8':
            laporan_ringkas()
        
        elif pilihan == '9':
            filename = input("Masukkan nama file untuk ekspor (default 'daftar_barang.txt'): ")
            if not filename:
                filename = "daftar_barang.txt"
            ekspor_ke_txt(filename)
        
        elif pilihan == '10':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memulai aplikasi
menu()
