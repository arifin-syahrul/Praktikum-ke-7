# Praktikum-ke-7

### Nama : Arifin Syahrul Azhadi Harahap

### NIM : 352310965

### Kelas : IE.23.C.13

### Mata Kuliah : Program Komputer + Praktek

### Dosen : Agung Nugroho, S.Kom., M.Kom.
_________________________________________________________________________________________________________________________________________________________________________________________

## "Membuat program sederhana pada pyhton menggunakan "List" dan "Dictionary"

## A. Algoritma Program

Algoritma Program Pengelolaan Nilai Mahasiswa

1, Mulai Program
  
2, Inisialisasi List Kosong
* students = [] (untuk menyimpan data mahasiswa)

3, Tampilkan Menu Utama 

o	Pilihan:
- Lihat Data (L)
- Tambah Data (T)
- Ubah Data (U)
- Hapus Data (H)
- Cari Data (C)
- Keluar (K)

4, Pilih Menu
 
o	Input pilihan pengguna.

#### Proses Berdasarkan Pilihan Menu

5, Jika Pilihan (L): Lihat Data
   
o	Jika list students kosong:
- Tampilkan pesan "Tidak Ada Data".

o	Jika list tidak kosong: 
- Tampilkan semua data mahasiswa dalam format tabel.

6, Jika Pilihan (T): Tambah Data
    
o	Input: 
- NIM
- Nama
- Nilai Tugas
- Nilai UTS
- Nilai UAS

o	Hitung Nilai Akhir: 
- nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

o	Tambahkan data ke dalam list students.

o	Tampilkan pesan "Data Berhasil Ditambahkan".

7, Jika Pilihan (U): Ubah Data
    
o	Tampilkan data mahasiswa.

o	Input nomor data yang ingin diubah.

o	Jika nomor valid: 
* Input data baru: 
* NIM, Nama, Tugas, UTS, UAS.
* Hitung ulang nilai akhir.
* Perbarui data dalam list.
* Tampilkan pesan "Data Berhasil Diubah".

o	Jika nomor tidak valid: 
* Tampilkan pesan "Nomor Data Tidak Valid".

8, Jika Pilihan (H): Hapus Data
    
o	Tampilkan data mahasiswa.

o	Input nomor data yang ingin dihapus.

o	Jika nomor valid: 
* Hapus data dari list students.
* Tampilkan pesan "Data Berhasil Dihapus".

o	Jika nomor tidak valid: 
* Tampilkan pesan "Nomor Data Tidak Valid".

9, Jika Pilihan (C): Cari Data
    
o	Input NIM mahasiswa yang ingin dicari.

o	Cari data berdasarkan NIM dalam list students.

o	Jika ditemukan: 
* Tampilkan data mahasiswa.

o	Jika tidak ditemukan: 
* Tampilkan pesan "Data Tidak Ditemukan".

10, Jika Pilihan (K): Keluar
    
o	Tampilkan pesan "Keluar dari Program".

o	Hentikan program.

11, Jika Pilihan Tidak Valid
    
o	Tampilkan pesan "Pilihan Tidak Valid".

o	Kembali ke menu utama.

12, Ulangi dari Langkah 3 Hingga Pengguna Memilih Keluar (K).
    
13, Selesai

## B. Gambar Flowchart Program

![Flowchart ke-7 drawio](https://github.com/user-attachments/assets/2351522e-4b0e-4d89-a8d9-596704697233)

## C. Menampilkan Program dan penjelasan Yang telah dibuat menggunakan program "Perulangan", "List" dan "Dictionary"

![Gambar Program 1](https://github.com/user-attachments/assets/6e45e984-61a6-4c8a-8e0d-d56bbd64238b)

![Gambar Program 2](https://github.com/user-attachments/assets/bee4f0b9-e2eb-4570-8c27-99cf1bba1d66)

![Gambar Program 3](https://github.com/user-attachments/assets/ee003d69-49c6-4137-b332-9aef2f4d64b6)

Berikut penjelasan programnya

1, Variabel students

Variabel students digunakan untuk menyimpan daftar data mahasiswa. Data ini berbentuk list yang berisi elemen-elemen berupa dictionary.
Setiap mahasiswa memiliki informasi:

* nim: Nomor Induk Mahasiswa.
* nama: Nama Mahasiswa.
* tugas: Nilai Tugas.
* uts: Nilai Ujian Tengah Semester (UTS).
* uas: Nilai Ujian Akhir Semester (UAS).
* akhir: Nilai Akhir (dihitung dari bobot nilai tugas, UTS, dan UAS).

2, Menu Utama

Program menampilkan menu utama dengan pilihan berikut:
* L (Lihat Data): Menampilkan data mahasiswa.
* T (Tambah Data): Menambahkan data baru.
* U (Ubah Data): Mengubah data mahasiswa yang sudah ada.
* H (Hapus Data): Menghapus data mahasiswa berdasarkan nomor.
* C (Cari Data): Mencari mahasiswa berdasarkan NIM.
* K (Keluar): Mengakhiri program.

3, Fungsi dalam Program

Program ini dibagi menjadi beberapa fungsi untuk menangani setiap tugas.

1. Fungsi display_data (Lihat Data)
* Menampilkan semua data mahasiswa dalam format tabel.
* Jika data kosong, ditampilkan pesan "Tidak Ada Data"

2. Fungsi add_data (Tambah Data)
* Meminta input dari pengguna untuk NIM, Nama, Nilai Tugas, UTS, dan UAS.
* Menghitung nilai akhir dengan rumus:

![image](https://github.com/user-attachments/assets/cf2a1a5f-9fa8-458a-8df1-0be88d2a9ed3)

* Menambahkan data baru ke list students.
* Menampilkan pesan "Data Berhasil Ditambahkan".

3. Fungsi update_data (Ubah Data)
* Menampilkan data yang ada.
* Meminta nomor data yang ingin diubah.
Jika nomor valid:
* Meminta input data baru.
* Menghitung ulang nilai akhir.
* Memperbarui data di list students.
* Menampilkan pesan "Data Berhasil Diubah".
Jika nomor tidak valid, ditampilkan pesan "Nomor Data Tidak Valid".

4. Fungsi delete_data (Hapus Data)
* Menampilkan data yang ada.
* Meminta nomor data yang ingin dihapus.
* Jika nomor valid, data dihapus dari list students.
* Menampilkan pesan "Data Berhasil Dihapus".
* Jika nomor tidak valid, ditampilkan pesan "Nomor Data Tidak Valid".

5. Fungsi search_data (Cari Data)
* Meminta NIM yang ingin dicari.
* Mencari mahasiswa dengan NIM tersebut dalam list students.
* Jika ditemukan, data mahasiswa ditampilkan.
* Jika tidak ditemukan, ditampilkan pesan "Data Tidak Ditemukan".

4, Alur Program
* Program terus berjalan dalam looping hingga pengguna memilih menu Keluar (K).
* Setiap pilihan dalam menu memanggil fungsi yang sesuai.

* Jika pengguna memasukkan pilihan yang tidak valid, program akan menampilkan pesan "Pilihan Tidak Valid" dan kembali ke menu utama.

5, Penghitungan Nilai Akhir

Nilai akhir dihitung dengan bobot sebagai berikut:
* 30% dari Nilai Tugas.
* 35% dari Nilai UTS.
* 35% dari Nilai UAS. Rumus:

![image](https://github.com/user-attachments/assets/c1b27351-3ea3-4410-b2fb-709fd12b7841)

6, Format Tampilan Data

Data mahasiswa ditampilkan dalam format tabel dengan kolom:
* No: Nomor urut data.
* NIM: Nomor Induk Mahasiswa.
* Nama: Nama mahasiswa.
* Tugas, UTS, UAS: Nilai masing-masing komponen.
* Akhir: Nilai akhir hasil perhitungan.
Contoh:

![image](https://github.com/user-attachments/assets/3db8bdbe-f392-4c15-be2b-77b2de0140d2)

7, Penanganan Kesalahan
* Jika data kosong, program menampilkan pesan "Tidak Ada Data".
* Jika nomor data tidak valid untuk mengubah atau menghapus, program menampilkan pesan "Nomor Data Tidak Valid".
* Jika NIM tidak ditemukan saat mencari, program menampilkan pesan "Data Tidak Ditemukan".
* Jika pengguna memilih menu yang tidak valid, program menampilkan pesan "Pilihan Tidak Valid".

## D. Hasil Program yang telah dijalankan dengan mengklik "Run"

![Hasil Program 1](https://github.com/user-attachments/assets/bc7fe569-2d8c-4531-9308-5d54e3888946)

![Hasil Program 2](https://github.com/user-attachments/assets/7604784c-44fc-4bbb-b4d9-050aeca16fa9)

### Selesai







