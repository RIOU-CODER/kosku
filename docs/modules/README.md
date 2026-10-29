# Peta Hubungan Antar Modul

Sistem Kosku dibagi menjadi 5 modul sesuai [D2: Module Breakdown](https://github.com/RIOU-CODER/kosku/blob/main/docs/D2_Rincian_Modul.md). Setiap modul punya satu dokumen yang berisi tanggung jawab, isi (data & aturan), hubungan dengan modul lain, dan alasan pengelompokan.

| No | Modul | Dokumen | Use case terkait (D3) |
| :-- | :--- | :--- | :--- |
| 1 | Autentikasi | [01_Autentikasi.md](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/1.Autentikasi.md) | UC-01, UC-02 |
| 2 | Manajemen Kamar | [02_Manajemen_Kamar.md](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/2.Manajemen_Kamar.md) | UC-03, UC-04, UC-05 |
| 3 | Tagihan & Pembayaran | [03_Tagihan_Pembayaran.md](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/3.Tagihan_Pembayaran.md) | UC-06 s.d. UC-11 |
| 4 | Tiket Keluhan | [04_Tiket_Keluhan.md](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/4.Tiket_Keluhan.md) | UC-12 s.d. UC-16 |
| 5 | Notifikasi | [05_Notifikasi.md](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/5.Notifikasi.md) | UC-17, UC-18 |

## Diagram Ketergantungan

Panah berarti "bergantung pada" (sesuai tabel ketergantungan di D2).

mermaid
flowchart TD
    Notif["5. Notifikasi"] --> Tagihan["3. Tagihan & Pembayaran"]
    Notif --> Tiket["4. Tiket Keluhan"]
    Tagihan --> Kamar["2. Manajemen Kamar"]
    Tagihan --> Auth["1. Autentikasi"]
    Tiket --> Kamar
    Tiket --> Auth
    Kamar --> Auth
    

## Catatan Arah Ketergantungan dan Arah Pemicu

Pada diagram di atas, Notifikasi *bergantung pada* Tagihan dan Tiket karena ia tidak punya pemicu sendiri. Namun saat sistem berjalan (lihat sequence diagram D4), *pemicu mengalir sebaliknya*: modul Tagihan atau Tiket memanggil modul Notifikasi ketika ada kejadian (tagihan jatuh tempo, tiket dibuat, status tiket berubah). Jadi Notifikasi bersifat pasif dan hanya bereaksi. Dengan begitu tidak ada ketergantungan melingkar, dan Notifikasi tetap berada di lapisan paling atas.

## Urutan Pengembangan yang Disarankan

Mengikuti arah ketergantungan, dari yang paling mendasar:

1. Autentikasi
2. Manajemen Kamar
3. Tagihan & Pembayaran dan Tiket Keluhan (bisa dikerjakan paralel, keduanya hanya butuh modul 1 dan 2)
4. Notifikasi

## Batasan Sistem (dari D1)

Semua modul tidak mencakup: pemrosesan pembayaran lewat payment gateway, chat waktu nyata, dan pencarian atau pemesanan kamar oleh calon penyewa eksternal.
