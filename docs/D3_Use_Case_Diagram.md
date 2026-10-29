# D3: Use Case Diagram

Satu diagram use case yang mencakup seluruh Sistem Kosku. Use case dikelompokkan berdasarkan 5 modul pada D2, dan seluruh aktor mengacu pada **Target Pengguna di D1**.

[Use Case Diagram](diagram/D3_Use_Case/Use_Case.png)

[Lihat Kode PlantUML](diagram/D3_Use_Case/Use_Case_Diagram.puml)

## Aktor (sesuai D1)

| Aktor | Peran dalam sistem |
| :--- | :--- |
| **Penyewa (Tenant)** | Melihat dan membayar tagihan sewa, membuat tiket keluhan, memantau status tiket, serta menerima pengingat tagihan. |
| **Pemilik Kos (Owner)** | Mengelola data kamar dan penempatan penyewa, menerbitkan tagihan, memantau pembayaran, serta memperbarui status tiket keluhan. |

## Daftar Use Case per Modul (18 use case)

| Modul (D2) | ID | Use Case | Aktor |
| :--- | :--- | :--- | :--- |
| Autentikasi | UC-01 | Login | Penyewa, Pemilik Kos |
| | UC-02 | Logout | Penyewa, Pemilik Kos |
| Manajemen Kamar | UC-03 | Kelola Data & Kapasitas Kamar | Pemilik Kos |
| | UC-04 | Tempatkan Penyewa ke Kamar | Pemilik Kos |
| | UC-05 | Perbarui Status Ketersediaan Kamar | (di-include oleh UC-04) |
| Tagihan & Pembayaran | UC-06 | Terbitkan Tagihan Bulanan | Pemilik Kos |
| | UC-07 | Lihat Tagihan Bulanan | Penyewa |
| | UC-08 | Bayar Tagihan | Penyewa |
| | UC-09 | Validasi Nominal Pembayaran | (di-include oleh UC-08) |
| | UC-10 | Hitung Denda Keterlambatan | (meng-extend UC-08) |
| | UC-11 | Pantau Status Pembayaran | Pemilik Kos |
| Tiket Keluhan | UC-12 | Buat Tiket Keluhan | Penyewa |
| | UC-13 | Validasi Nomor Kamar | (di-include oleh UC-12) |
| | UC-14 | Lihat Status Tiket | Penyewa |
| | UC-15 | Perbarui Status Tiket | Pemilik Kos |
| | UC-16 | Lacak Riwayat Kerusakan Kamar | Pemilik Kos |
| Notifikasi | UC-17 | Kirim Notifikasi Tiket | (di-include oleh UC-12 dan UC-15) |
| | UC-18 | Kirim Pengingat Tagihan & Keterlambatan | Penyewa (penerima, dipicu sistem) |

## Penjelasan Relasi `<<include>>` dan `<<extend>>`

**`<<include>>`** dipakai untuk perilaku yang **selalu** dijalankan oleh use case dasar (sesuai alur pada D4):

| Relasi | Alasan |
| :--- | :--- |
| UC-04 Tempatkan Penyewa → UC-05 Perbarui Status Kamar | Setiap penempatan penyewa selalu mengubah status ketersediaan kamar. |
| UC-08 Bayar Tagihan → UC-09 Validasi Nominal | Setiap pembayaran selalu divalidasi nominalnya sebelum status menjadi Lunas. |
| UC-12 Buat Tiket Keluhan → UC-13 Validasi Nomor Kamar | Setiap tiket baru wajib dikaitkan dengan nomor kamar yang valid. |
| UC-12 dan UC-15 → UC-17 Kirim Notifikasi Tiket | Pembuatan tiket (notifikasi ke pemilik) dan pembaruan status tiket (notifikasi ke penyewa) selalu memicu notifikasi. UC-17 dipakai bersama oleh dua use case. |

**`<<extend>>`** dipakai untuk perilaku yang **opsional / bersyarat**:

| Relasi | Kondisi |
| :--- | :--- |
| UC-10 Hitung Denda Keterlambatan → UC-08 Bayar Tagihan | Hanya berjalan jika pembayaran dilakukan setelah jatuh tempo. Jika tepat waktu, UC-08 selesai tanpa UC-10. |

## Catatan

* Login (UC-01) merupakan prasyarat bagi semua use case lain yang membutuhkan hak akses, sehingga tidak digambarkan sebagai `<<include>>` di setiap use case agar diagram tetap terbaca.
* Sesuai batasan ruang lingkup D1, tidak ada use case untuk pembayaran via *payment gateway*, *chat* waktu nyata, maupun pencarian kamar oleh calon penyewa publik.
