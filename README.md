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
* [D2: Rincian_Modul](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/README.md)
* [D3: Use_Case_Diagram](https://github.com/RIOU-CODER/kosku/blob/main/docs/D3_Use_Case_Diagram.md)
* [D4: Sequence_Diagrams](https://github.com/RIOU-CODER/kosku/blob/main/docs/D4_Sequence_Diagram.md)
* [D5: Activity Log](https://github.com/RIOU-CODER/kosku/blob/main/ACTIVITY_LOG.md)
* [D6: Test Case Design](https://github.com/RIOU-CODER/kosku/blob/main/docs/D6_Test_Cases.md)
* [D7: Sourcode](https://github.com/RIOU-CODER/kosku/tree/main/src)

**[Peta Hubungan Antar Modul](https://github.com/RIOU-CODER/kosku/blob/main/docs/modules/README.md)**
   Sistem dipecah menjadi 5 modul untuk menghindari tumpang tindih aturan:
  
## 🛠️ Instruksi Menjalankan Pengujian (D7)
Kami menggunakan `pytest` untuk menguji fungsi kalkulasi denda keterlambatan pembayaran (`calculate_late_fee`). 

**Langkah-langkah pengujian:**
1. Pastikan sistem Anda sudah terpasang Python 3.
2. Instal *framework* pengujian dengan perintah: 
   ```bash
   pip install pytest


## 🤖 Kebijakan Penggunaan AI (AI Usage Policy)
Sesuai dengan ketentuan proyek, kami menggunakan bantuan AI dengan rincian sebagai berikut:

Gemini AI: Digunakan sebagai rekan diskusi (brainstorming) untuk memecah masalah ke dalam modul-modul sistem, merancang draf logika edge cases pada tabel pengujian, serta membantu menyusun kerangka syntax dasar PlantUML untuk Sequence Diagram.

Semua keluaran diagram, kasus uji, dan logika kode telah kami tinjau secara manual, direvisi, dan kami pertanggungjawabkan sepenuhnya agar sesuai dengan konteks aplikasi Kosku.



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
|           ├── usecase.jpeg                <-- (Gambar hasil D3)
|           └── usecase.puml                <-- (Kode sumber D3)
|       └── D4_Sequence_Diagram
|           ├── Alur_Autentikasi.puml             <-- (Kode sumber D4 - Skenario 1)
|           ├── Alur_Autentikasi.png              <-- (Gambar hasil D4 - Skenario 1)
|           ├── Alur_Management_Kamar.puml        <-- (Kode sumber D4 - Skenario 2)
|           ├── Alur_Management_Kamar.png         <-- (Gambar hasil D4 - Skenario 2)
|           ├── Alur_Tagihan_Pembayaran.puml      <-- (Kode sumber D4 - Skenario 3)
|           ├── Alur_Tagihan_Pembayaran.png       <-- (Gambar hasil D4 - Skenario 3)
|           ├── Alur_Tiket_Keluhan.puml           <-- (Kode sumber D4 - Skenario 4)
|           ├── Alur_Tiket_Keluhan.png            <-- (Gambar hasil D4 - Skenario 4)
|           ├── Alur_Notifikasi.puml              <-- (Kode sumber D4 - Skenario 5)
|           └── Alur_Notifikasi.png               <-- (Gambar hasil D4 - Skenario 5)
|   └── modules/
|       ├── 1.Autentikasi.md            <-- (Penjelasan tentang module 1)
|       ├── 2.Manajemen_Kamar.md        <-- (Penjelasan tentang module 2)
|       ├── 3.Tagihan_Pembayaran.md     <-- (Penjelasan tentang module 3)
|       ├── 4.Tiket_Keluhan.md          <-- (Penjelasan tentang module 4)
|       ├── 5.Notifikasi.md             <-- (Penjelasan tentang module 5)
|
├── src/
|   ├── Hasil_code_pytest.png          <-- (Gambar hasil dari code yang di test)
|   ├── billing.py                     <-- (Kode implementasi fungsi D7)
|   └── test_billing.py                <-- (Kode unit test menggunakan pytest D7)
|
├── ACTIVITY_LOG.md                    <-- (Catatan log aktivitas tim beserta link commit/PR)
└── README.md                          <-- (Halaman utama berisi nama tim dan link ke semua file)
```
