# Kosku: Sistem Manajemen Kos
**Anggota Tim:**
1. Ryandra Yusuf - 26110300022 - @RIOU-CODER
2. Zafirah Bintang Maya - 26110300036 - @zafirahbintangkay
3. Shofyanto Qodaeary - 26110300016 - @shofyantoqodaery

*Catatan: Sebagian draf dokumen dan kode pengujian dibuat dengan bantuan AI, lalu direvisi oleh tim.*

## D1. Topic & Problem Statement
**Deskripsi:** Kosku adalah aplikasi manajemen kos yang membantu pemilik dan penyewa melacak tagihan, riwayat pembayaran, dan laporan perbaikan kamar secara terpusat.
**Masalah:** Saat ini, pemilik kos mencatat tagihan dan keluhan melalui obrolan WhatsApp dan buku catatan fisik[cite: 4]. Metode ini menyebabkan pembayaran sering terlewat, laporan kerusakan kamar tertumpuk atau hilang, dan tidak ada transparansi riwayat transaksi bagi penyewa.
**Aktor:** Pemilik Kos, Penyewa Kos[cite: 4].
**Ruang Lingkup:** Aplikasi ini akan mencatat tagihan, memvalidasi bukti transfer, dan mengelola tiket komplain. Aplikasi **tidak** akan melakukan: 1) Pencarian kos untuk pengguna luar, 2) Pemrosesan *payment gateway* otomatis, 3) Obrolan (*chat*) *real-time*.

## D2. Module Breakdown
* **Authentication:** Menangani login dan sesi[cite: 4]. (Fitur: Login, Reset Password).
* **Room Management:** Mengelola data kamar dan penghuni[cite: 4]. (Fitur: Tambah kamar, Assign penyewa).
* **Billing & Payment:** Membuat tagihan dan mencatat pembayaran[cite: 4]. (Fitur: Tagihan otomatis, Hitung denda).
* **Complaint Ticketing:** Menangani laporan kerusakan[cite: 4]. (Fitur: Buat tiket, Update status).
* **Notification:** Mengirim peringatan[cite: 4]. (Fitur: Reminder jatuh tempo).
**Dependensi:** Semua modul bergantung pada *Authentication*; *Billing* bergantung pada *Room Management*.

## D4. Sequence Diagram (Skenario 1: Membayar Sewa)
**Alasan penting:** Pembayaran sewa adalah fungsi utama untuk memastikan kelancaran arus kas kos.

```mermaid
sequenceDiagram
    actor Penyewa
    participant UI as Aplikasi UI
    participant Auth as Auth Module
    participant Bill as Billing Module
    
    Penyewa->>UI: Pilih tagihan & upload bukti
    UI->>Auth: Cek sesi login
    Auth-->>UI: Sesi valid
    UI->>Bill: Submit bukti
    alt Bukti valid
        Bill-->>UI: Status Menunggu Verifikasi
    else Format salah
        Bill-->>UI: Error Format tidak didukung
    end
