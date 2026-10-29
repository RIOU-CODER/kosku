# Modul 2: Manajemen Kamar (Room Management)

*Use case terkait (D3):* UC-03 Kelola Data & Kapasitas Kamar, UC-04 Tempatkan Penyewa ke Kamar, UC-05 Perbarui Status Ketersediaan Kamar  
*Sequence diagram (D4):* Alur_Management_Kamar

## 1. Tanggung Jawab

* Menjadi pusat data fisik kos: daftar kamar dan kapasitasnya.
* Mengatur *penempatan penyewa* ke kamar tertentu.
* Menjaga *status ketersediaan* kamar agar selalu sesuai dengan kondisi penempatan.
* Menyediakan data kamar yang valid bagi modul Tagihan dan Tiket Keluhan.

## 2. Isi Modul

### Data

| Data | Keterangan |
| :--- | :--- |
| Kamar | Nomor kamar, kapasitas, status ketersediaan (misalnya Tersedia / Terisi / Penuh) |
| Alokasi penempatan | Hubungan antara penyewa dan kamar yang ditempati |

### Aturan

* Hanya *Pemilik Kos* yang boleh menambah atau mengubah data kamar dan menempatkan penyewa. Akses divalidasi lewat modul Autentikasi.
* Kamar baru otomatis berstatus *Tersedia*.
* Setiap penempatan penyewa *selalu memperbarui status* kamar (Terisi atau Penuh sesuai kapasitas). Karena itu UC-04 meng-include UC-05 di diagram D3.
* Nomor kamar harus unik agar bisa dirujuk oleh tagihan dan tiket keluhan.

## 3. Hubungan dengan Modul Lain

| Arah | Modul | Bentuk hubungan |
| :--- | :--- | :--- |
| Bergantung pada | Autentikasi | Membutuhkan validasi identitas Pemilik untuk menambah atau mengubah data kamar. |
| Dipakai oleh | Tagihan & Pembayaran | Tagihan sewa dikaitkan dengan data kamar dan penyewa yang menempatinya. |
| Dipakai oleh | Tiket Keluhan | Setiap keluhan harus merujuk ke nomor kamar yang valid. |

## 4. Alasan Pengelompokan

Pencatatan kamar, penempatan penyewa, dan status ketersediaan dikelompokkan karena ketiganya *mengubah dan membaca data yang sama*: kondisi fisik dan alokasi kamar. Status ketersediaan tidak bisa berdiri sendiri karena ia adalah akibat langsung dari penempatan. Dengan satu modul sebagai sumber data kamar, modul Tagihan dan Tiket Keluhan cukup bertanya ke satu tempat dan tidak perlu menyimpan salinan data kamar sendiri.
