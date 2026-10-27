# D2: Module Breakdown

Sistem aplikasi Kosku dikelompokkan ke dalam 5 modul utama yang saling berinteraksi untuk memenuhi alur kerja pengelolaan kos.

## 1. Autentikasi (Auth)
Modul ini bertanggung jawab untuk mengelola akses masuk pengguna dan mengamankan data berdasarkan peran sistem. Modul ini secara tegas memisahkan hak akses antara penyewa dan pemilik kos.
*   Fitur utama:
    *   *Login* dan *Logout* pengguna.
    *   Manajemen sesi pengguna (penyewa vs. pemilik).

## 2. Manajemen Kamar (Room Management)
Modul ini berfungsi sebagai pusat data fisik kos untuk mengatur ketersediaan dan status alokasi kamar. 
*   Fitur utama:
    *   Pencatatan data dan kapasitas kamar.
    *   Penempatan penyewa ke dalam kamar tertentu.
    *   Pembaruan status ketersediaan kamar.

## 3. Tagihan & Pembayaran (Billing & Payment)
Modul ini mengelola pencatatan arus kas operasional kos, memastikan setiap tagihan terbayar dan terekam dengan akurat.
*   Fitur utama:
    *   Penerbitan tagihan sewa bulanan.
    *   Pencatatan status pembayaran (lunas/belum lunas).
    *   Kalkulasi denda keterlambatan secara otomatis.

## 4. Tiket Keluhan (Complaint Ticketing)
Modul ini mengubah keluhan tidak terstruktur menjadi sistem tiket yang terorganisir untuk memfasilitasi pelaporan kerusakan fasilitas.
*   Fitur utama:
    *   Pembuatan tiket keluhan perbaikan oleh penyewa.
    *   Pembaruan status pengerjaan tiket oleh pemilik.
    *   Pelacakan riwayat kerusakan kamar.

## 5. Notifikasi (Notification)
Modul ini mengambil alih komunikasi penagihan manual dengan memberikan pemberitahuan dan pengingat otomatis kepada sistem.
*   Fitur utama:
    *   Pengiriman pengingat batas waktu tagihan.
    *   Peringatan keterlambatan pembayaran sewa.
    *   Pemberitahuan pembaruan status tiket keluhan.

## Ketergantungan Antarmodul

Berikut adalah tabel rincian bagaimana modul-modul di atas saling bergantung satu sama lain di dalam sistem:

| Modul | Bergantung Pada | Alasan Ketergantungan |
| :--- | :--- | :--- |
| **Autentikasi** | Tidak ada | Merupakan modul dasar yang memvalidasi akses; tidak bergantung pada logika bisnis modul lain. |
| **Manajemen Kamar** | Autentikasi | Membutuhkan validasi identitas pemilik untuk menambah/mengubah data kamar. |
| **Tagihan & Pembayaran** | Manajemen Kamar, Autentikasi | Perlu data kamar untuk menagih sewa, dan Autentikasi untuk memvalidasi hak akses penyewa saat membayar. |
| **Tiket Keluhan** | Manajemen Kamar, Autentikasi | Keluhan harus dikaitkan dengan pelapor yang valid (Autentikasi) dan nomor kamar spesifik (Manajemen Kamar). |
| **Notifikasi** | Tagihan, Tiket Keluhan | Memerlukan pemicu (trigger) dari modul tagihan (tenggat waktu) atau tiket (status berubah) untuk mengirim pesan. |
