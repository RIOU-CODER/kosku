# D4: Sequence Diagrams

Dokumen ini memuat 5 skenario utama dari aplikasi Kosku. Setiap skenario digambarkan melalui *Sequence Diagram* yang mencakup interaksi antara aktor, antarmuka pengguna (UI), modul sistem, basis data, beserta alur alternatif penanganan kesalahannya.

## 1. Penyewa Membayar Sewa Bulanan
* **Dikerjakan oleh:** Ryandra Yusuf
* **Alasan Pentingnya Skenario:** Skenario ini sangat krusial karena mencatat arus kas utama operasional kos dan memvalidasi nominal transaksi secara sistem, sehingga memastikan tidak ada pembayaran yang terlewat atau kurang dari jumlah tagihan[cite: 4].

![Sequence Diagram Pembayaran](assets/seq_pembayaran.png)
*(Catatan: Kode sumber PlantUML tersimpan di `assets/seq_pembayaran.puml`)*

## 2. Penyewa Mengajukan Keluhan Perbaikan
* **Dikerjakan oleh:** Shofyanto Qodaery
* **Alasan Pentingnya Skenario:** Skenario ini mengubah proses pelaporan kerusakan dari sekadar pesan obrolan WhatsApp yang mudah tenggelam menjadi sistem tiket resmi yang terstruktur[cite: 4]. Hal ini memastikan setiap keluhan dapat dilacak status pengerjaannya oleh penyewa dan pemilik.

![Sequence Diagram Keluhan](assets/seq_keluhan.png)
*(Catatan: Kode sumber PlantUML tersimpan di `assets/seq_keluhan.puml`)*

## 3. Pemilik Mengirim Pengingat Tagihan
* **Dikerjakan oleh:** zafirah Bintang Maya
* **Alasan Pentingnya Skenario:** Skenario ini mengotomatiskan tugas penagihan manual berdasarkan batas waktu (*due date*) pembayaran[cite: 4]. Dengan fitur ini, risiko penunggakan dapat dikurangi karena sistem akan mengirimkan pengingat secara tepat waktu kepada penyewa yang belum lunas.

![Sequence Diagram Pengingat](assets/seq_pengingat.png)
*(Catatan: Kode sumber PlantUML tersimpan di `assets/seq_pengingat.puml`)*
