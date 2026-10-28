# Kosku - Sistem Manajemen Kos 

Proyek ini adalah repositori tugas Final Exam (UAS) untuk mata kuliah Software Development Fundamentals. Kosku adalah aplikasi pencatatan administrasi yang membantu pemilik kos dan penyewa mengelola tagihan sewa bulanan serta melacak status keluhan perbaikan fasilitas secara terpusat.

## 👥 Anggota Tim
1. **Ryandra Yusuf** 
   - NIM: [26110300022] 
   - GitHub: [@RIOU-CODER](https://github.com/RIOU-CODER)
2. **Shofyanto Qodaery** 
   - NIM: [26110300036] 
   - GitHub: [@shofyantoqodaery](https://github.com/shofyantoqodaery)
3. **Zafirah Bintang Maya** 
   - NIM: [26110300016] 
   - GitHub: [@zafirahbintangkay](https://github.com/zafirahbintangkay)

## 📂 Daftar Kiriman (Deliverables)
Berikut adalah tautan menuju seluruh dokumen rancangan sistem dan kode pengujian kami:
* [D1: Topik_Masalah](https://github.com/RIOU-CODER/kosku/blob/main/docs/D1_Topik_Masalah.md)
* [D2: Rincian_Modul](https://github.com/RIOU-CODER/kosku/blob/main/docs/D2_Rincian_Modul.md)
* [D3: Use_Case_Diagram](https://github.com/RIOU-CODER/kosku/blob/main/docs/D3_Use_Case_Diagram.md)
* [D4: Sequence_Diagrams](https://github.com/RIOU-CODER/kosku/blob/main/docs/D4_Sequence_Diagram.md)
* [D5: Activity Log](https://github.com/RIOU-CODER/kosku/blob/main/ACTIVITY_LOG.md)
* [D6: Test Case Design](https://github.com/RIOU-CODER/kosku/blob/main/docs/D6_Test_Cases.md)
* [D7: Unit-Tested Code](src/billing.py)

## 🛠️ Instruksi Menjalankan Pengujian (D7)
Kami menggunakan `pytest` untuk menguji fungsi kalkulasi denda keterlambatan pembayaran (`calculate_late_fee`). 

**Langkah-langkah pengujian:**
1. Pastikan sistem Anda sudah terpasang Python 3.
2. Instal *framework* pengujian dengan perintah: 
   ```bash
   pip install pytest
   
```text
   /kosku_project_repo
|
├── docs/
|   ├── D1_Topic_Problem.md            <-- (Pernyataan masalah dan ruang lingkup)
|   ├── D2_Module_Breakdown.md         <-- (Rincian 5 modul aplikasi)
|   ├── D3_UseCase.md                  <-- (Halaman penampilkan tautan ke Use Case Diagram png & puml)
|   ├── D4_Sequence.md                 <-- (Halaman penampilkan 5 tautan Sequence Diagram png & puml)
|   ├── D6_Test_Cases.md               <-- (Tabel 10 kasus uji)
|   └── diagram/                        
|       └── D3_Use_Case
            ├── usecase.puml               <-- (Kode sumber D3)
|           └── usecase.png                <-- (Gambar hasil D3)
        └── D4_Sequence_Diagram
|           ├── seq_Alur_Autentikasi.puml             <-- (Kode sumber D4 - Skenario 1)
|           ├── seq_Alur_Autentikasi.png              <-- (Gambar hasil D4 - Skenario 1)
|           ├── seq_Alur_Management_Kamar.puml        <-- (Kode sumber D4 - Skenario 2)
|           ├── seq_Alur_Management_Kamar.png         <-- (Gambar hasil D4 - Skenario 2)
|           ├── seq_Alur_Tagihan_Pembayaran.puml      <-- (Kode sumber D4 - Skenario 3)
|           ├── seq_Alur_Tagihan_Pembayaran.png       <-- (Gambar hasil D4 - Skenario 3)
|           ├── seq_Alur_Tiket_Keluhan.puml           <-- (Kode sumber D4 - Skenario 4)
|           ├── seq_Alur_Tiket_Keluhan.png            <-- (Gambar hasil D4 - Skenario 4)
|           ├── seq_Alur_Notifikasi.puml              <-- (Kode sumber D4 - Skenario 5)
|           └── seq_Alur_Notifikasi.png               <-- (Gambar hasil D4 - Skenario 5)
|
├── src/
|   ├── billing.py                     <-- (Kode implementasi fungsi D7)
|   └── test_billing.py                <-- (Kode unit test menggunakan pytest D7)
|
├── ACTIVITY_LOG.md                    <-- (Catatan log aktivitas tim beserta link commit/PR)
└── README.md                          <-- (Halaman utama berisi nama tim dan link ke semua file)
```
