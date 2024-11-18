# Program Pendataan Barang Rental Event Organizer dengan Fitur Login, Register, dan Peran Admin/User

# Daftar pengguna untuk menyimpan data akun dan peran mereka (hanya admin yang memiliki akun bawaan)
pengguna = {
    "admin": {"password": "admin123", "role": "admin"}
}

# Fungsi untuk registrasi pengguna baru (hanya untuk peran user)
def registrasi():
    print("\n=== Registrasi Pengguna Baru ===")
    nama_lengkap = input("Masukkan nama lengkap: ")
    username = input("Masukkan username: ")
    if username in pengguna:
        print("Username sudah terdaftar. Silakan gunakan username lain.")
        return
    password = input("Masukkan password: ")
    pengguna[username] = {'password': password, 'role': 'user', 'nama_lengkap': nama_lengkap}
    print(f"Registrasi berhasil. Akun pengguna '{username}' berhasil dibuat. Silakan login untuk melanjutkan.")

# Fungsi untuk login
def login():
    print("\n=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in pengguna and pengguna[username]['password'] == password:
        print(f"Login berhasil sebagai {pengguna[username]['role']}.")
        return username
    else:
        print("Username atau password salah.")
        return None

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
    ekspor_ke_txt()  # Memanggil ekspor langsung setelah edit barang



# Fungsi untuk melihat semua barang yang ada di daftar
def lihat_barang():
    if not daftar_barang:
        print("Belum ada barang yang terdaftar.")
    else:
        print("\nDaftar Barang:")
        for idx, barang in enumerate(daftar_barang, start=1):
            print(f"{idx}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}, Status: {barang['Status']}")
            
def edit_barang():
    if not daftar_barang:
        print("Daftar barang kosong. Tidak ada barang untuk diedit.")
        return

    nama_barang = input("Masukkan nama barang yang ingin diedit: ").strip()

    barang_found = None
    for barang in daftar_barang:
        if barang['Nama'].lower() == nama_barang.lower():
            barang_found = barang
            break

    if not barang_found:
        print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")
        return

    nama_baru = input(f"Masukkan nama baru ({barang_found['Nama']}): ").strip() or barang_found['Nama']
    kategori_baru = input(f"Masukkan kategori baru ({barang_found['Kategori']}): ").strip() or barang_found['Kategori']
    try:
        harga_baru = int(input(f"Masukkan harga sewa baru (Rp{barang_found['Harga Sewa']}): ").strip()) or barang_found['Harga Sewa']
    except ValueError:
        print("Harga sewa tidak valid. Menggunakan nilai lama.")
        harga_baru = barang_found['Harga Sewa']
    status_baru = input(f"Masukkan status baru ({barang_found['Status']}): ").strip() or barang_found['Status']

    # Perbarui data barang
    barang_found['Nama'] = nama_baru
    barang_found['Kategori'] = kategori_baru
    barang_found['Harga Sewa'] = harga_baru
    barang_found['Status'] = status_baru

    print(f"Barang '{nama_barang}' berhasil diperbarui.")
    ekspor_ke_txt()  # Memanggil ekspor langsung setelah edit barang


# Fungsi untuk menghapus barang dari daftar
def hapus_barang(nama):
    for barang in daftar_barang:
        if barang['Nama'].lower() == nama.lower():
            daftar_barang.remove(barang)
            print(f"Barang '{nama}' berhasil dihapus.")
            return
    print(f"Barang dengan nama '{nama}' tidak ditemukan.")
    ekspor_ke_txt()  # Memanggil ekspor langsung setelah edit barang

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
    
#user 
def pinjam_barang(username):
    if 'barang_dipinjam' not in pengguna[username]:
        pengguna[username]['barang_dipinjam'] = []  # Pastikan kunci tersedia

    print("Daftar Barang:")
    for index, barang in enumerate(daftar_barang):
        # Pastikan menggunakan huruf kapital yang sesuai
        print(f"{index + 1}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}, Status: {barang['Status']}")

    nama_barang = input("Masukkan nama barang yang ingin dipinjam: ").strip()
    for barang in daftar_barang:
        if barang['Nama'].lower() == nama_barang.lower() and barang['Status'].lower() == 'tersedia':
            pengguna[username]['barang_dipinjam'].append(barang)
            barang['Status'] = 'Dipinjam'
            print(f"Barang {barang['Nama']} berhasil dipinjam!")
            return

    print("Barang tidak ditemukan atau tidak tersedia.")
    ekspor_ke_txt()  # Memanggil ekspor langsung setelah edit barang


# Fungsi untuk melihat koleksi barang yang dipinjam oleh user
def koleksi_barang_dipinjam(username):
    barang_dipinjam = pengguna[username]['barang_dipinjam']
    if not barang_dipinjam:
        print("Anda belum meminjam barang apapun.")
    else:
        print("\nKoleksi Barang yang Dipinjam:")
        for idx, barang in enumerate(barang_dipinjam, start=1):
            print(f"{idx}. Nama: {barang['Nama']}, Kategori: {barang['Kategori']}, Harga Sewa: Rp{barang['Harga Sewa']}")
    ekspor_ke_txt()  # Memanggil ekspor langsung setelah edit barang

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
        
# Fungsi untuk menampilkan menu admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Barang")
        print("2. Edit Barang")
        print("3. Hapus Barang")
        print("4. Lihat Daftar Barang")
        print("5. Cari Barang")
        print("6. Urutkan Barang Berdasarkan Nama")
        print("7. Hitung Barang per Kategori")
        print("8. Tampilkan Laporan Ringkas")
        print("9. Ekspor Data ke File TXT")
        print("10. Logout")
        
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
            edit_barang()
            
        elif pilihan == '3':
            nama = input("Masukkan nama barang yang ingin dihapus: ")
            hapus_barang(nama)        
       
        elif pilihan == '4':
            lihat_barang()
            
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
            print("Logout berhasil.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu user
def menu_user(username):
    while True:
        print("\n=== Menu User ===")
        print("1. Lihat Daftar Barang")
        print("2. Cari Barang")
        print("3. Pinjam Barang")
        print("4. Koleksi Barang")
        print("5. Logout")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            lihat_barang()
        
        elif pilihan == '2':
            keyword = input("Masukkan kata kunci pencarian (nama/kategori): ")
            cari_barang(keyword)
        
        elif pilihan == '3':
            pinjam_barang(username)
        
        elif pilihan == '4':
            koleksi_barang_dipinjam(username)
        
        elif pilihan == '5':
            print("Logout berhasil.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi utama untuk login, registrasi, dan akses menu berdasarkan peran
def main():
    while True:
        print("\n=== Dashboard Aplikasi Rental Barang Event Organizer ===")
        print("1. Login")
        print("2. Registrasi (Hanya untuk User)")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            username = login()
            if username:
                role = pengguna[username]['role']
                if role == 'admin':
                    menu_admin()
                elif role == 'user':
                    menu_user(username) 
        
        elif pilihan == '2':
            registrasi()
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memulai aplikasi
main()