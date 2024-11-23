# Membuat dictionary daftar kontak
daftar_kontak = {
    "Ari": "08123456789",
    "Dina": "08234567890",
    "Budi": "08345678901"
}

# Tampilkan kontaknya Ari
print("Kontak Ari:", daftar_kontak.get("Ari"))

# Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak["Riko"] = "087654544"
print("Kontak Riko ditambahkan.")

# Ubah kontak Dina dengan nomor baru 088999776
daftar_kontak["Dina"] = "088999776"
print("Nomor Dina telah diperbarui.")

# Tampilkan semua Nama
print("Daftar Nama:", list(daftar_kontak.keys()))

# Tampilkan semua Nomor
print("Daftar Nomor:", list(daftar_kontak.values()))

# Tampilkan daftar Nama dan nomornya
print("Daftar Kontak:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Hapus kontak Dina
if "Dina" in daftar_kontak:
    del daftar_kontak["Dina"]
    print("Kontak Dina telah dihapus.")
else:
    print("Kontak Dina tidak ditemukan.")

# Tampilkan daftar kontak setelah penghapusan
print("Daftar Kontak setelah penghapusan:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")
