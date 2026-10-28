# Modul 4: Tiket Keluhan (Complaint Ticketing)

*Use case terkait (D3):* UC-12 Buat Tiket Keluhan, UC-13 Validasi Nomor Kamar, UC-14 Lihat Status Tiket, UC-15 Perbarui Status Tiket, UC-16 Lacak Riwayat Kerusakan Kamar  
*Sequence diagram (D4):* Alur_Tiket_Keluhan

## 1. Tanggung Jawab

* Mengubah keluhan yang tadinya tidak terstruktur (obrolan dan catatan) menjadi *tiket* yang terorganisir.
* Memungkinkan Penyewa melaporkan kerusakan fasilitas dan memantau perkembangannya.
* Memungkinkan Pemilik memperbarui status pengerjaan tiket.
* Menyimpan *riwayat kerusakan* per kamar.

## 2. Isi Modul

### Data

| Data | Keterangan |
| :--- | :--- |
| Tiket keluhan | ID tiket, pelapor (Penyewa), nomor kamar, judul, deskripsi, foto, status, waktu dibuat dan diperbarui |
| Riwayat tiket per kamar | Kumpulan tiket yang pernah dibuat untuk suatu kamar, sebagai catatan riwayat kerusakan |

### Aturan

* Tiket hanya bisa dibuat oleh *Penyewa yang sudah login* (sesi valid).
* Tiket *wajib dikaitkan dengan nomor kamar yang valid. Validasi dilakukan lewat modul Manajemen Kamar (UC-13, di-*include oleh UC-12).
* Tiket baru otomatis berstatus *Pending*.
* Status tiket hanya boleh diubah oleh *Pemilik Kos*, misalnya menjadi "Sedang Diperbaiki" atau "Selesai".
* Pembuatan tiket dan perubahan status tiket *selalu memicu notifikasi* (ke Pemilik saat tiket dibuat, ke Penyewa saat status berubah).

## 3. Hubungan dengan Modul Lain

| Arah | Modul | Bentuk hubungan |
| :--- | :--- | :--- |
| Bergantung pada | Autentikasi | Keluhan harus dikaitkan dengan pelapor yang valid. |
| Bergantung pada | Manajemen Kamar | Keluhan harus dikaitkan dengan nomor kamar yang spesifik dan valid. |
| Dipakai oleh | Notifikasi | Menjadi pemicu pemberitahuan tiket baru dan perubahan status tiket. |

## 4. Alasan Pengelompokan

Pembuatan tiket, pembaruan status, dan pelacakan riwayat dikelompokkan karena semuanya berputar pada *satu objek yang sama, yaitu tiket*, dengan siklus hidup yang jelas (Pending sampai Selesai). Modul ini dipisah dari Tagihan karena datanya, aktor pemicunya, dan aturan bisnisnya berbeda sama sekali. Perubahan pada cara menangani keluhan tidak perlu menyentuh logika keuangan, begitu juga sebaliknya.
