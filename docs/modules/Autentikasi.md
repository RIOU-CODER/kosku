# Modul 1: Autentikasi (Auth)

*Use case terkait (D3):* UC-01 Login, UC-02 Logout  
*Sequence diagram (D4):* Alur_Autentikasi

## 1. Tanggung Jawab

* Memverifikasi identitas pengguna saat login dan mengakhiri sesi saat logout.
* Menentukan *peran* pengguna (Penyewa atau Pemilik Kos) dan menyimpannya di sesi.
* Menjadi pintu pengaman bagi modul lain: memastikan setiap permintaan datang dari sesi yang valid dan dengan peran yang berhak.
* Memisahkan hak akses secara tegas antara Penyewa dan Pemilik Kos.

## 2. Isi Modul

### Data

| Data | Keterangan |
| :--- | :--- |
| Pengguna | ID pengguna, username/email, hash password, peran (Penyewa / Pemilik) |
| Sesi / token | Token sesi (JWT atau session) yang membawa ID pengguna dan peran, serta status aktif/nonaktif |

### Aturan

* Password disimpan dalam bentuk hash, bukan teks asli. Login dicocokkan terhadap hash tersebut.
* Login berhasil hanya jika kredensial cocok. Hasilnya adalah token beserta data peran.
* Setelah login, pengguna diarahkan ke dashboard sesuai perannya (Penyewa atau Pemilik).
* Logout menonaktifkan token sesi, lalu pengguna kembali ke halaman login.
* Hak akses ditentukan oleh peran:
  * *Pemilik Kos:* mengelola kamar, menerbitkan tagihan, memperbarui status tiket.
  * *Penyewa:* melihat dan membayar tagihan sendiri, membuat tiket keluhan.

## 3. Hubungan dengan Modul Lain

| Arah | Modul | Bentuk hubungan |
| :--- | :--- | :--- |
| Bergantung pada | Tidak ada | Modul dasar, tidak bergantung pada logika bisnis modul lain. |
| Dipakai oleh | Manajemen Kamar | Memvalidasi bahwa yang mengubah data kamar adalah Pemilik. |
| Dipakai oleh | Tagihan & Pembayaran | Memvalidasi hak akses Penyewa saat membayar. |
| Dipakai oleh | Tiket Keluhan | Memastikan pelapor tiket adalah pengguna yang valid. |

## 4. Alasan Pengelompokan

Login, logout, dan pengelolaan sesi dikelompokkan karena ketiganya mengurus satu hal yang sama, yaitu *siapa pengguna ini dan apa haknya*. Memisahkannya dari modul lain membuat aturan keamanan hanya perlu ditulis dan diubah di satu tempat, bukan tersebar di setiap fitur. Karena modul ini tidak bergantung pada logika bisnis kos, ia menjadi fondasi yang dikerjakan lebih dulu.
