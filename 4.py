# Program Daftar Nilai Mahasiswa

# Inisialisasi dictionary untuk menyimpan data mahasiswa
daftar_nilai = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    daftar_nilai[nim] = {'Nama': nama, 'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
    print(f"Data mahasiswa dengan NIM {nim} berhasil ditambahkan.")

def ubah_data():
    nim = input("Masukkan NIM yang ingin diubah: ")
    if nim in daftar_nilai:
        print(f"Data saat ini: {daftar_nilai[nim]}")
        tugas = float(input("Masukkan Nilai Tugas baru: "))
        uts = float(input("Masukkan Nilai UTS baru: "))
        uas = float(input("Masukkan Nilai UAS baru: "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        daftar_nilai[nim] = {'Nama': daftar_nilai[nim]['Nama'], 'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
        print(f"Data mahasiswa dengan NIM {nim} berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")

def hapus_data():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in daftar_nilai:
        del daftar_nilai[nim]
        print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

def tampilkan_data():
    if daftar_nilai:
        print("Daftar Nilai Mahasiswa:")
        for nim, data in daftar_nilai.items():
            print(f"NIM: {nim}, Nama: {data['Nama']}, Tugas: {data['Tugas']}, UTS: {data['UTS']}, UAS: {data['UAS']}, Nilai Akhir: {data['Nilai Akhir']:.2f}")
    else:
        print("Belum ada data mahasiswa.")

def cari_data():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in daftar_nilai:
        data = daftar_nilai[nim]
        print(f"NIM: {nim}, Nama: {data['Nama']}, Tugas: {data['Tugas']}, UTS: {data['UTS']}, UAS: {data['UAS']}, Nilai Akhir: {data['Nilai Akhir']:.2f}")
    else:
        print("NIM tidak ditemukan.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()