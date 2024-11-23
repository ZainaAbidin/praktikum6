# Penjelasan Praktikum
1. Program ini dirancang untuk mengelola data nilai mahasiswa menggunakan struktur data dictionary 
di Python. Dalam program ini, data mahasiswa disimpan dengan NIM sebagai kunci, dan nilai 
yang terkait berupa sub-dictionary yang berisi informasi seperti nama, nilai tugas, UTS, UAS, dan nilai akhir.

2. Salah satu fungsi penting dalam program adalah hitung_nilai_akhir, yang bertugas menghitung 
nilai akhir mahasiswa. Perhitungan ini didasarkan pada bobot tertentu, yaitu 30% untuk tugas, 35% 
untuk UTS, dan 35% untuk UAS. Hasil dari fungsi ini akan digunakan untuk menyimpan nilai akhir mahasiswa dalam dictionary.

3. Ketika pengguna ingin menambahkan data mahasiswa, fungsi tambah_data meminta input berupa 
NIM, nama, dan nilai tugas, UTS, serta UAS. Setelah nilai akhir dihitung menggunakan fungsi 
hitung_nilai_akhir, data mahasiswa disimpan ke dalam dictionary daftar_nilai dengan struktur
yang telah ditentukan. Fungsi ini juga memberikan notifikasi keberhasilan setelah data ditambahkan.

4. Jika ada data mahasiswa yang perlu diubah, pengguna dapat menggunakan fungsi ubah_data. 
Fungsi ini meminta NIM mahasiswa yang ingin diubah. Jika NIM ditemukan dalam dictionary, 
program akan menampilkan data saat ini, lalu meminta pengguna memasukkan nilai baru. Data 
kemudian diperbarui, termasuk nilai akhirnya yang dihitung ulang. Jika NIM tidak ditemukan, 
program akan memberikan pesan kesalahan.

5. Untuk menghapus data, program menyediakan fungsi hapus_data. Pengguna diminta memasukkan 
NIM yang ingin dihapus. Jika NIM ditemukan, data mahasiswa akan dihapus dari dictionary. Jika 
tidak ditemukan, program akan menampilkan pesan bahwa NIM tidak ada.

6. Fungsi tampilkan_data digunakan untuk mencetak semua data mahasiswa yang tersimpan. Jika 
ada data, program akan menampilkan seluruhnya dalam format tabel. Namun, jika dictionary kosong, 
program akan memberi tahu bahwa belum ada data yang dimasukkan.

7. Pencarian data mahasiswa dapat dilakukan dengan fungsi cari_data. Pengguna hanya perlu 
memasukkan NIM, dan jika NIM ditemukan, data mahasiswa akan ditampilkan. Sebaliknya, 
jika NIM tidak ditemukan, program akan memberikan pesan kesalahan.

8. Semua fungsi ini diakses melalui fungsi utama menu. Fungsi ini berisi antarmuka yang 
memungkinkan pengguna memilih berbagai operasi, seperti menambah data, 
mengubah data, menghapus data, menampilkan semua data, mencari data, atau keluar dari program. Jika pengguna 
memilih untuk keluar, program akan berhenti. Jika pengguna memberikan input yang tidak valid, 
program akan meminta mereka untuk mencoba lagi.

9. Secara keseluruhan, program berjalan dalam lingkaran hingga pengguna memutuskan untuk keluar. 
Ini memastikan semua operasi dapat dilakukan secara berulang tanpa perlu menjalankan ulang 
program. Dengan sistem seperti ini, program menjadi alat yang efisien untuk mengelola data 
mahasiswa.
